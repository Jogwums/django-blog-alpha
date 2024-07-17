from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])

# later   
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()