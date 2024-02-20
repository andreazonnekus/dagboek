from distutils.command.upload import upload
from email.policy import default
from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from avatar.models import Avatar
from django.core.files import File
from django.conf import settings
from avatar.models import AvatarField

import msal, requests, json

class UserManager(AbstractUserManager):
    pass

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=80)
    email = models.EmailField(unique=True, max_length=254)
    # avatar = AvatarField(upload_to='avatars/', default='')

    first_name = models.CharField(blank=True, max_length=80)
    last_name = models.CharField(blank=True, max_length=80)
    # timezone = 
    birthdate =  models.DateField(blank=True)
    # preferred_language = models.
    def __str__(self) -> str:
        return self.username

        