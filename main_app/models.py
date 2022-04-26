from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your models here.

GENRES = [
    ("Hip-hop","Hip-hop"),
    ("Go-go","Go-go"),
    ("Dance","Dance"),
    ("Electronic","Electronic"),
    ("Metal","Metal")
]

EVENT_IMAGES =[
("https://i.imgur.com/lRoQdnp.jpg", "Pink Room with Tree"),
("https://i.imgur.com/PHkcUmE.jpg", "Light Exhibit and Dark Male Sillhouette"),
("https://i.imgur.com/7jzYmng.jpg", "Art Gallery"),
("https://i.imgur.com/NLFOoET.jpg", "Dinosaur Skeleton Exhibit"),
("https://i.imgur.com/1kCMaKp.jpg", "Neon Globe Exhibit"),
("https://i.imgur.com/nlcBzWk.jpg", "Street Projector Art"),
("https://i.imgur.com/r1oFmIj.jpg", "Neon Hallway"),
("https://i.imgur.com/WJRdvrB.jpg", "Portrait Behind Wet Glass"),
("https://i.imgur.com/Z2G7Rq8.jpg", "Kaleidoscope Portrait"),
("https://i.imgur.com/BgYsieG.jpg7", "Neon Entrance"),
("https://i.imgur.com/rggt66b.jpg", "The Matrix Aesthetic"),
("https://i.imgur.com/x68h9hP.jpg", "It's Inside Us All")
]

#EVENT MODEL : id, owner, photo url, title,long description, date, location, genres

class Event(models.Model):
    title = models.CharField(max_length=500)
    genres = models.CharField(max_length=50, choices = GENRES)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=250)
    img_2 = models.CharField(max_length=1000, choices = EVENT_IMAGES)
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
