from django.db import models
from django.forms import CharField, IntegerField


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)


