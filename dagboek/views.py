from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
  template = loader.get_template('home.html')

  return HttpResponse(template.render())

def about_me(request):
  template = loader.get_template('about_me.html')

  return HttpResponse(template.render())

def about_meitian(request):
  template = loader.get_template('about_meitian.html')

  return HttpResponse(template.render())