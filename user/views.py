import msal

from django.core.cache import cache
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from .custom_auth_backend import *



# def login(request):


def logout(request):
    # Clear out the user and token
    remove_user_and_token(request)

    return HttpResponseRedirect(reverse_lazy('home'))

def msallogin(request):
    msal_instance = MSALAuthBackend() 

    # Redirect to the Azure sign-in page
    return msal_instance.init_auth(request)

def callback(request):

    #TODO: if msal
    auth_code = request.GET.get('code')
    msal_instance = MSALAuthBackend() 
    user = msal_instance.authenticate(request, auth_code=auth_code)

    if user:
        return render(request, 'home.html')    
    else:
        return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})