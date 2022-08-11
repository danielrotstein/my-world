from django.db import models

# Create your models here.


class ScubaDiving(models.Model):
    location = models.CharField(max_length=150)
    equipment = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)

    interest = models.ForeignKey(
        "interests.Interest",
        related_name="interests",
        on_delete=models.CASCADE, null=True,
    )

    def __str__(self):
        return self.location
