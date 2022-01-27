from django.db import models

from django.utils import timezone

# Create your models here.

class stock_port(models.Model) :
    name = models.TextField()
    price = models.TextField(null=True)
    quantity = models.TextField(null=True)

class crypto_port(models.Model) :
    name = models.TextField()
    price = models.TextField(null=True)
    quantity = models.TextField(null=True)