from django.db import models
from django.utils import timezone

# Create your models here.

class Scrapbook(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    start_date = models.DateField(default = timezone.now)
    frequency = models.IntegerField(default = 0)
    every = models.IntegerField(default = 0)
    mode = models.IntegerField(default = 0)
    email = models.EmailField(max_length = 50, blank = True, null = True, unique = True)

    def __init(self, name, description, start_date, frequency, every, mode, email):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.frequency = frequency
        self.every = every
        self.mode = mode
        self.email = email

class Picture(models.Model):
    name = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 20)
    date = models.DateTimeField()
