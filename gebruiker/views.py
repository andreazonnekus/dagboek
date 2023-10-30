from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gebruiker

def inteken(request):
  template = loader.get_template('inteken.html')

  return HttpResponse(template.render())

def registrasie(request):
  template = loader.get_template('registreer.html')
  
  context = {
    'registreer': Inskrywing.objects.all().values()
  }

  return HttpResponse(template.render())
# Create your views here.