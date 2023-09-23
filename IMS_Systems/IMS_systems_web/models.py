from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    User            = models.OneToOneField(User, on_delete=models.CASCADE)

class Services (models.Model):
    id                  = models.AutoField(primary_key=True)
    Service_name        = models.CharField(max_length=200, default=None, blank=True, null=True)
    Image               = models.ImageField(default=None, blank=True, null=True)
    web_ink             = models.URLField(default=None, blank=True, null=True)
    Description         = models.CharField(max_length=2500, default=None, blank=True, null=True)
    Short_Description   = models.CharField(max_length=250,default=None, blank=True, null=True)

class Products (models.Model):
    id                  = models.AutoField(primary_key=True)
    Product_name        = models.CharField(max_length=200, default=None, blank=True, null=True)
    Image               = models.ImageField(default=None, blank=True, null=True)
    web_ink             = models.URLField(default=None, blank=True, null=True)
    Description         = models.CharField(max_length=2500, default=None, blank=True, null=True)
    Short_Description   = models.CharField(max_length=250,default=None, blank=True, null=True)