import msal

from django.core.cache import cache
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout, views

from .forms import *
from .models import CustomUser
from .custom_auth_backend import *

class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user/signup.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)

        return redirect(self.success_url)

class CustomSigninView(views.LoginView):
    template_name = 'user/signin.html'
    redirect_authenticated_user = True

class CustomSignOutView(views.LogoutView):
    template_name = 'user/signout.html'
    
    def form_valid(self, form):
        remove_user_and_token(request)
        logout(request)

def msallogin(request):
    msal_instance = MSALAuthBackend() 
    auth_app = get_msal_app()

    # Redirect to the Azure sign-in page
    return msal_instance.init_auth(request, auth_app)

def callback(request):

    #TODO: if msal
    auth_code = request.GET.get('code')
    auth_app = get_msal_app()

    msal_instance = MSALAuthBackend() 
    msal_instance.authenticate(request, auth_app, auth_code=auth_code)