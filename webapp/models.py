from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.
class Scrapbook(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    start_date = models.DateField(default = timezone.now)
    frequency = models.IntegerField(default = 0)
    every = models.IntegerField(default = 0)
    mode = models.IntegerField(default = 0)
    email = models.EmailField(max_length = 50, blank = True)


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class Picture(models.Model):
    scrapbook = models.ForeignKey(Scrapbook)
    name = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 20)
    date = models.DateTimeField()
    pic = models.ImageField(upload_to = 'assets/scrapbooks/', default = 'assets/no-img.jpg')