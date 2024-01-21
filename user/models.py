from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from avatar.models import Avatar
from django.core.files import File
from django.conf import settings
from avatar.models import AvatarField

import msal, requests, json

class CustomUser(AbstractUser):

    username = models.CharField(unique=True, max_length=80)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)
    # avatar = AvatarField(upload_to='avatars/', default='')

    def __str__(self) -> str:
        return self.username
    
    def get_or_create_user(email = None, username = None, access_token = None):
        

# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser)
#     avatar = models.ImageField

        