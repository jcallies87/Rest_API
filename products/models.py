from django.db import models
from django.forms import IntegerField

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()
    