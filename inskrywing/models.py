from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Inskrywing(models.Model):
    tietel = models.CharField(max_length=255)
    inhoud = models.TextField
    skeppings_tyd = models.DateTimeField

    def __str__(self) -> str:
        return self.tietel

    #class Meta:
    #    verbose_name_plural = "Inskrywings"
