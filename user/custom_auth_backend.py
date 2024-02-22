from typing import Any
from django.contrib.auth import get_user_model, login
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpRequest
from msal import ConfidentialClientApplication

from .utils import *

class MSALAuthBackend(ModelBackend):
    # def authenticate(self, request: Optional[HttpRequest], **kwargs: Any) -> Optional[AbstractBaseUser]:
    def init_auth(self, request: HttpRequest, auth_app, **kwargs: Any):

        cache = load_cache(request)
        
        auth_url = auth_app.get_authorization_request_url(
            scopes = settings.APP_SCOPES,
            redirect_uri = settings.REDIRECT_URL)
        
        return redirect(auth_url)

    @receiver(setting_changed)
    def authenticate(self, request: HttpRequest, auth_app, auth_code=None, **kwargs: Any):
        User = get_user_model()

        if auth_code is None:
            return None

        token_response = auth_app.acquire_token_by_authorization_code(
            code = auth_code,
            scopes = settings.APP_SCOPES,
            redirect_uri = settings.REDIRECT_URL
        )

        if 'access_token' and 'id_token_claims' in token_response:
            claims = token_response.get('id_token_claims', {})

            # already authenticated
            if request.user.is_authenticated:
                
                return request.user

            if 'email' in claims and is_email(claims.get('email').split('#')[0]):
                email = claims.get('email').split('#')[0]
            elif 'preferred_username' in claims and is_email(claims.get('preferred_username')):
                email = claims.get('preferred_username')

            if email:
                try:
                    user = User.objects.get(email = email)
                except User.DoesNotExist:
                    # TODO: Consider moving this out to a separate function
                    user = User(email = email)
                    user.is_staff = False
                    user.is_superuser = False
                    user.set_unusable_password()
                    user.save()
                    login(request, user)
                    return user
            
        return None
