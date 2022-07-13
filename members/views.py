from tokenize import Name
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = request.POST['name']
  y = request.POST['genre']
  z = request.POST['year']
  member = Members(Name=x, Genre=y, Year=z)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  moviename = request.POST['name']
  moviegenre = request.POST['genre']
  movieyear = request.POST['year']
  member = Members.objects.get(id=id)
  member.name = moviename
  member.genre = moviegenre
  member.year = movieyear
  member.save()
  return HttpResponseRedirect(reverse('index'))
