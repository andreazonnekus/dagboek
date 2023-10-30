from django.db import models
from django.contrib.auth.models import AbstractUser

class Gebruiker(AbstractUser):
    gebruikersNaam = models.CharField(unique=True, max_length=80)
    epos = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)

    USERNAME_FIELD = 'gebruikersNaam'

    def __str__(self) -> str:
        return self.gebruikersNaam
# Create your models here.
