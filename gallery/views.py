from django.shortcuts import render

def index(req):
  return render(req, 'gallery/index.html')

def image(req): 
  return render(req, 'gallery/image.html')
