from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpRequest
from msal import ConfidentialClientApplication

from .utils import *
from .models import CustomUser

class MSALAuthBackend(ModelBackend):
    # def authenticate(self, request: Optional[HttpRequest], **kwargs: Any) -> Optional[AbstractBaseUser]:
    def init_auth(self, request: HttpRequest, **kwargs: Any):
        # Check for a token cache in the session
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
                request = request,
                claims = token_response.get('id_token_claims', {}),
                access_token = token_response['access_token'])
            self.msal_login(request, user)
            return user

        return None
    
    def msal_login(self, request, user):

        pass

    def get_or_create_user(self, request, claims, access_token):
        User = get_user_model()

        # If the user is authenticated, return
        if request.user.is_authenticated:
            return request.user
        
        if 'email' in claims:
            user, created = User.objects.get_or_create_user(email = claims.get('email'), access_token = access_token)
        elif 'preferred_username' in claims:
            user, created = User.objects.get_or_create_user(username = claims.get('preferred_username'), access_token = access_token)

        return user