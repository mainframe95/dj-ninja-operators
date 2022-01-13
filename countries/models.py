from django.db import models
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=250, unique=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=timezone.now)
