import datetime	
from distutils.command.upload import upload
from email.policy import default
from hashlib import new
from types import CoroutineType
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class bikes(models.Model): 
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    new = models.BooleanField(default= False)
    city = models.CharField(max_length=60)
    price = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics/')
    username = models.CharField(max_length=200)
    catagory = models.CharField(max_length=7, default='bikes', editable=False)
    disable = models.BooleanField(default= False)

class cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    new = models.BooleanField(default= False)
    city = models.CharField(max_length=60)
    price = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    username = models.CharField(max_length=200)
    catagory = models.CharField(max_length=7, default='cars', editable=False)
    disable = models.BooleanField(default= False)
class laptops(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    new = models.BooleanField(default= False)
    city = models.CharField(max_length=60)
    price = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    username = models.CharField(max_length=200)
    catagory = models.CharField(max_length=7, default='laptops', editable=False)
    disable = models.BooleanField(default= False)
class mobiles(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    new = models.BooleanField(default= False)
    city = models.CharField(max_length=60)
    price = models.IntegerField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    username = models.CharField(max_length=200)
    catagory = models.CharField(max_length=7, default='mobiles', editable=False)
    disable = models.BooleanField(default= False)

class User_info(models.Model):
    User_name = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=100)
    user_address = models.CharField(max_length=200)
    user_email = models.EmailField()


class Buyer_info(models.Model):
    Buyer_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    product_id = models.IntegerField()
    Product_name = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.datetime.now() , editable=False)
    EndTime = models.DateTimeField(default=datetime.datetime.now()+ datetime.timedelta(hours=1) , editable=False)
    varification = models.BooleanField(default=False)
    
class Rating(models.Model):    
    buyer_id = models.IntegerField()
    Buyer_name = models.CharField(max_length=100)
    Product_catagory = models.CharField(max_length=100)
    product_id = models.IntegerField()
    time = models.DateTimeField(default=datetime.datetime.now() , editable=False)
    rate = models.IntegerField(blank=True)
    comment = models.CharField(max_length=250, blank=True)

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    Details = models.CharField(max_length=300, blank=True)