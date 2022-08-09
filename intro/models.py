from django.db import models

# User settings
from django.conf import settings

# Create your models here.

class Intro(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="intro",
        null=True,
        on_delete=models.SET_NULL,
    )

