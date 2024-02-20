import msal

from django.core.cache import cache
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView


from .forms import *
from .models import CustomUser
from .custom_auth_backend import *

class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'

    def get_absolute_url(self):
        return 'home.html'

# def login(request):

def logout(request):
    # Clear out the user and token
    remove_user_and_token(request)

    return HttpResponseRedirect(reverse_lazy('home'))

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
    user = msal_instance.authenticate(request, auth_app, auth_code=auth_code)

    request.session.modified = True
    print(request.user)
    return HttpResponseRedirect(reverse_lazy('home'))

# def signup(request):
#     print(request.session)
#     if request.method == 'POST':
#         f = CustomUserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('register')

#     else:
#         f = CustomUserCreationForm()

#     return render(request, 'registration/register.html', {'form': f})