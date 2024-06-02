from django.shortcuts import render, get_object_or_404, redirect
from gallery.models import Photo
from django.contrib import messages

def index(req):
  if not req.user.is_authenticated:
    messages.error(req, 'Para ter acesso, você precisa estar logado.')
    return redirect('login')
  
  photos = Photo.objects.order_by("date").filter(published=True)
  return render(req, 'gallery/index.html', {"cards": photos})

def image(req, photo_id): 
  photo = get_object_or_404(Photo, pk=photo_id)
  return render(req, 'gallery/image.html', {"photo": photo})

def search(req):
  if not req.user.is_authenticated:
    messages.error(req, 'Para ter acesso à busca, você precisa estar logado.')
    return redirect('login')
  
  photos = Photo.objects.order_by("date").filter(published=True)

  if "search" in req.GET:
    search_name = req.GET['search']
    if search_name:
      photos = photos.filter(name__icontains=search_name)

  return render(req, 'gallery/search.html', {"cards": photos})


