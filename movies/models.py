from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)
    overview = models.TextField()
    movie_info = models.TextField()
    my_review = models.TextField()
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name