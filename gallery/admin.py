from django.contrib import admin
from gallery.models import Photo

# Register your models here.

class ListPhotos(admin.ModelAdmin):
  list_display = ("id", "name", "subtitle", "published")
  list_display_links = ("id", "name")
  search_fields = ("name",)
  list_filter = ("category",)
  list_per_page = 10
  list_editable = ("published",)

admin.site.register(Photo, ListPhotos)
