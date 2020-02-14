from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    Image_url = models.CharField(max_length=2086)
    

class offer (models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
