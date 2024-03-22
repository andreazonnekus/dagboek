from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.urls import reverse
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from time import timezone

class UserManager(AbstractUserManager):
    pass

class CustomUser(AbstractUser):
    username=models.CharField(unique=True, max_length=80)
    email=models.EmailField(unique=True, max_length=254)
    # user_auth_type=models.CharField(choices=)
    # avatar=AvatarField(upload_to='avatars/', default='')

    # timezone=
    can_use_timezone = models.BooleanField(default = True)
    birthdate = models.DateField(blank=True, null=True)

    # preferred_language=models.
    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        return reverse('user:profile', kwargs={'pk': self.pk})
    

# class Profile(models.Model):
#     user=models.OneToOneField(CustomUser)
#     avatar=models.ImageField
        
