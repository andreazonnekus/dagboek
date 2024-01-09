from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=80)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.username