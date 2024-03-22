from django.urls import path, include
from . import views

app_name='user'

urlpatterns=[
    path('signin', views.CustomSigninView.as_view(), name='signin'),
    path('signout', views.CustomSignOutView.as_view(), name='signout'),
    path('msallogin', views.msallogin, name='msal_login'),
    path('callback', views.callback, name='callback'),
    path('signup', views.CustomUserCreateView.as_view(), name='signup'),
    path('<int:pk>', views.CustomUserProfileView.as_view(), name='profile'),
    path('password_change', views.CustomUserPasswordChangeView.as_view(), name='password_change'),
    path('', include('django_sso.sso_service.urls')),
    # TODO: replacement for all default auth views
]
