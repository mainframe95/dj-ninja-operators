from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# User Model

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password= models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []