from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

""" def login(request):
  template = loader.get_template('login.html')

  return HttpResponse(template.render())
 """
def registration(request):
  template = loader.get_template('register.html')
  
  # context = {
  #   'register': Registration.objects.all().values()
  # }

  return HttpResponse(template.render())
# Create your views here.