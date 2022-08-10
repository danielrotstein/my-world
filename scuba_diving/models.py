from django.db import models

# Create your models here.

class ScubaDiving(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    equipment = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    