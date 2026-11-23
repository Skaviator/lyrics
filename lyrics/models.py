from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Lyrics(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) # właściciel
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.title} - {self.artist.name}"

class Translation(models.Model):
    lyrics = models.ForeignKey(Lyrics, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lyrics.title} - {self.lyrics.artist} : {self.author}"
