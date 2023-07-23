from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Inskrywing

def inskrywing(request):
  template = loader.get_template('inskrywing.html')
  
  context = {
    'inskrywings': Inskrywing.objects.all().values()
  }

  return HttpResponse(template.render(context))
# Create your views here.
