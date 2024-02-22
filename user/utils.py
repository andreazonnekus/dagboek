# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import msal, requests, json

from django.conf import settings


# graph helper
graph_url = 'https://graph.microsoft.com/v1.0'

is_email = lambda email: email.__contains__('@') and email.__contains__('.')
is_msal = lambda uri: uri.find("msal") !=-1

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


def remove_user_and_token(request):
    if 'token_cache' in request.session:
        del request.session['token_cache']