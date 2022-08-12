from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)
    overview = models.TextField()
    movie_info = models.TextField()
    year = models.CharField(null=True, max_length=10)
    genre = models.CharField(null=True, max_length=50)
    director = models.CharField(null=True, max_length=50)
    producer = models.CharField(null=True, max_length=50)
    runtime = models.CharField(null=True, max_length=50)
    my_review = models.TextField()
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
