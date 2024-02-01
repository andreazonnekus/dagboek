from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpRequest
from msal import ConfidentialClientApplication

from .utils import *

class MSALAuthBackend(ModelBackend):
    # def authenticate(self, request: Optional[HttpRequest], **kwargs: Any) -> Optional[AbstractBaseUser]:
    def init_auth(self, request: HttpRequest, **kwargs: Any):

        cache = load_cache(request)
        auth_app = get_msal_app()
        
        auth_url = auth_app.get_authorization_request_url(
            scopes = settings.APP_SCOPES,
            redirect_uri = settings.REDIRECT_URL)
        
        return redirect(auth_url)

    def authenticate(self, request: HttpRequest, auth_code=None, **kwargs: Any):

        if auth_code is None:
            return None

        auth_app = get_msal_app()

        token_response = auth_app.acquire_token_by_authorization_code(
            code = auth_code,
            scopes = settings.APP_SCOPES,
            redirect_uri = settings.REDIRECT_URL
        )

        if 'access_token' and 'id_token_claims' in token_response:
            user = self.get_or_create_user(
                is_msal = True,
                request = request,
                token_response = token_response
                )
            self.msal_login(request, user)
            return user

        return None
    
    def msal_login(self, request, user):


        # time_zone = user.get('mailboxSettings')['timeZone'] if (user.get('mailboxSettings') is not None) else 'UTC'
    
        # request.session['user'] = {
        #     'is_authenticated': True,
        #     'name': user['displayName'],
        #     'email': user['mail'] if (user['mail'] is not None) else user['userPrincipalName'],
        #     'timeZone': time_zone
        # }

        request.session.modified = True

        pass

    def get_or_create_user(self, is_msal, request, token_response):
        User = get_user_model()

        # claims = token_response.get('id_token_claims', {}),
        # get('access_token')

        # Get information from MSAL Graph

        # print(f'claims {claims}')
        # If the user is authenticated, return
        if request.user.is_authenticated:
            return request.user

            if 'email' in claims:
                email = claims.get('email').split('#')[0] if is_email(claims.get('email').split('#')[0]) else None
            
            if 'preferred_username' in claims:
                if not email:
                    email = claims.get('preferred_username') if is_email(claims.get('preferred_username')) else None
                uname = claims.get('preferred_username') if not is_email(claims.get('preferred_username')) else None
            
            if email:
                user = User.objects.get_or_create(email = email, username = uname)
        if user:
            return user

        return None