from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from users.models import User
from countries.models import Country

user = User

class Operator(models.Model):
    name = models.CharField(max_length=250, unique=True)
    clients = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=timezone.now)
    country = ForeignKey(to=Country, on_delete=models.CASCADE)
    createdBy = ForeignKey(to=User, on_delete=models.CASCADE)
