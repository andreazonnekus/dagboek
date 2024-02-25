from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name='user'

urlpatterns=[
    path('signin', views.CustomSigninView.as_view(), name='signin'),
    path('signout', views.CustomSignOutView.as_view(), name='signout'),
    path('msallogin', views.msallogin, name='msal_login'),
    path('callback', views.callback, name='callback'),
    path('signup', views.CustomUserCreateView.as_view(), name='signup'),
    # TODO: replacement for all default auth views
]
