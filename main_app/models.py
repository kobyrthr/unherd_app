from django.db import models

# Create your models here.

GENRES = [
    ("Hip-hop","hh"),
    ("Go-go","gg"),
    ("Dance","d"),
    ("Electronic","e"),
    ("Metal","m")
]

#EVENT MODEL : id, owner, photo url, title,long description, date, location, genres

class Event(models.Model):
    title = models.CharField(max_length=500)
    genres = models.CharField(max_length=50, choices = GENRES)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=250)
    date = models
