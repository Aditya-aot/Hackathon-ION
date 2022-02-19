from django.db import models
from django.conf import settings
from django.contrib.auth.models import User , auth 

from django.utils import timezone

# Create your models here.

class stock_port(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    name = models.TextField(null = True)
    price = models.TextField(null=True)
    quantity = models.TextField(null=True)

class crypto_port(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    name = models.TextField(null = True)
    price = models.TextField(null=True)
    quantity = models.TextField(null=True)