from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.template import loader

from user.auth_helper import (get_sign_in_flow, get_token_from_code, store_user,
    remove_user_and_token, get_token)

from .models import User

def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    # Save the expected flow so we can use it in the callback
    request.session['auth_flow'] = flow

    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])

def callback(request):
    # Make the token request
    result = get_token_from_code(request)

    #Get the user's profile
    user = get_user(result['access_token'])

    # Store user
    store_user(request, user)
    return HttpResponseRedirect(reverse_lazy('home'))

def sign_out(request):
    # Clear out the user and token
    remove_user_and_token(request)

    return HttpResponseRedirect(reverse_lazy('home'))

def registration(request):
  template = loader.get_template('user/register.html')
  
  # context = {
  #   'register': Registration.objects.all().values()
  # }

  return HttpResponse(template.render())