from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    path('', include("django.contrib.auth.urls")),
    path('msallogin', views.msallogin, name='msal_login'),
    path('callback', views.callback, name='callback'),
    path('registration', views.registration, name='registration'),
]