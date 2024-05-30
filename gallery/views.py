from django.shortcuts import render, get_object_or_404
from gallery.models import Photo

def index(req):
  photos = Photo.objects.order_by("date").filter(published=True)
  return render(req, 'gallery/index.html', {"cards": photos})

def image(req, photo_id): 
  photo = get_object_or_404(Photo, pk=photo_id)
  return render(req, 'gallery/image.html', {"photo": photo})
