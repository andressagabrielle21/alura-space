from django.db import models
from datetime import datetime

# Create your models here.

class Photo(models.Model):
  CATEGORY_OPTIONS = [
    ("NEBULOSA", "Nebulosa"),
    ("ESTRELA", "Estrela"),
    ("GALÁXIA", "Galáxia"),
    ("PLANETA", "Planeta")
  ]

  name = models.CharField(max_length=100, null=False, blank=False)
  subtitle = models.CharField(max_length=150, null=False, blank=False)
  category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, null=False, default='')
  description = models.TextField(null=False, blank=False)
  image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
  published = models.BooleanField(default=False)
  date = models.DateTimeField(default=datetime.now, blank=False)


  def __str__(self):
    return self.name
