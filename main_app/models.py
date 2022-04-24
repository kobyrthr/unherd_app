from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

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
    img_2 = models.ImageField(upload_to='images/')
    date = models
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

class RSVP(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
