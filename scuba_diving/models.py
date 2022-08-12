from django.db import models

# Create your models here.


class ScubaDiving(models.Model):
    location = models.CharField(max_length=150)
    equipment = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    image2 = models.URLField(null=True, blank=True)
    image3 = models.URLField(null=True, blank=True)
    image4 = models.URLField(null=True, blank=True)
    image5 = models.URLField(null=True, blank=True)
    languages = models.CharField(null=True, max_length=50)
    currency = models.CharField(null=True, max_length=50)
    timezone = models.CharField(null=True, max_length=50)
    best_time = models.TextField(null=True)

    interest = models.ForeignKey(
        "interests.Interest",
        related_name="interests",
        on_delete=models.CASCADE, null=True,
    )

    def __str__(self):
        return self.location
