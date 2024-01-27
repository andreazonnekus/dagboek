from distutils.command.upload import upload
from email.policy import default
from time import timezone
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
    # timezone = 

    def __str__(self) -> str:
        return self.username
    
    # def get_or_create_user(email = None, username = None, access_token = None):
        # time_zone = user.get('mailboxSettings')['timeZone'] if (user.get('mailboxSettings') is not None) else 'UTC'
    
        # request.session['user'] = {
        #     'is_authenticated': True,
        #     'name': user['displayName'],
        #     'email': user['mail'] if (user['mail'] is not None) else user['userPrincipalName'],
        #     'timeZone': time_zone
        # }

        # request.session.modified = True


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser)
#     avatar = models.ImageField

        