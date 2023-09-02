from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 255,unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4)
    
    