from django.db import models

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120) # required
    description     = models.TextField(blank=True, null=True) # not required
    price           = models.DecimalField(decimal_places=2, max_digits=10000) # required
    summary         = models.TextField(blank=False, null=False) # required
    featured        = models.BooleanField() # null=True, default=True