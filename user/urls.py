from django.urls import path, include
from . import views

urlpatterns = [
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
    path("accounts/", views.registration, name='registration'),
]