from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def tuis(request):
  template = loader.get_template('tuis.html')

  return HttpResponse(template.render())