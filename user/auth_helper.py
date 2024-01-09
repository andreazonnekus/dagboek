# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import msal, requests, json

from django.conf import settings


# graph helper
graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
    # Send GET to /me
    user = requests.get(
        '{0}/me'.format(graph_url),
        headers={
            'Authorization': 'Bearer {0}'.format(token)
        },
        params={
            # '$select': 'displayName,mail,mailboxSettings,userPrincipalName'
            '$select': 'displayName,mail,userPrincipalName'
        }
    )
    # Return the JSON result
    return user.json()

def load_cache(request):
    # Check for a token cache in the session
    cache = msal.SerializableTokenCache()
    if request.session.get('token_cache'):
        cache.deserialize(request.session['token_cache'])

    return cache

def save_cache(request, cache):
    # If cache has changed, persist back to session
    if cache.has_state_changed:
        request.session['token_cache'] = cache.serialize()

def get_msal_app(cache=None):
    # Initialize the MSAL confidential client
    auth_app = msal.ConfidentialClientApplication(
        settings.APP_ID,
        authority=settings.AUTHORITY,
        client_credential=settings.APP_SECRET,
        token_cache=cache)

    return auth_app

# Method to generate a sign-in flow
def get_sign_in_flow():
    auth_app = get_msal_app()

    return auth_app.initiate_auth_code_flow(
        settings.APP_SCOPES,
        redirect_uri=settings.REDIRECT_URL)

# Method to exchange auth code for access token
def get_token_from_code(request):
    cache = load_cache(request)
    auth_app = get_msal_app(cache)

    # Get the flow saved in session
    flow = request.session.pop('auth_flow', {})

    result = auth_app.acquire_token_by_auth_code_flow(flow, request.GET)
    save_cache(request, cache)

    return result

def store_user(request, user):
    time_zone = user.get('mailboxSettings')['timeZone'] if (user.get('mailboxSettings') is not None) else 'UTC'
    
    request.session['user'] = {
        'is_authenticated': True,
        'name': user['displayName'],
        'email': user['mail'] if (user['mail'] is not None) else user['userPrincipalName'],
        'timeZone': time_zone
    }

def get_token(request):
    cache = load_cache(request)
    auth_app = get_msal_app(cache)

    accounts = auth_app.get_accounts()
    if accounts:
        result = auth_app.acquire_token_silent(
            settings.APP_SCOPES,
            account=accounts[0])

        save_cache(request, cache)

        return result['access_token'] if result is not None else None

def remove_user_and_token(request):
    if 'token_cache' in request.session:
        del request.session['token_cache']

    if 'user' in request.session:
        del request.session['user']