from django.db import models

# User settings
from django.conf import settings

# Create your models here.

class Interest(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="interests",
        on_delete=models.CASCADE,
        null=True,
    )
    description = models.TextField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name + " by " + str(self.author)
