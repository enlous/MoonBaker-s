from django.db import models


# Create your models here.

class userdb(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.IntegerField(null=True, blank=True)
    CPassword = models.IntegerField(null=True, blank=True)

class ORDERdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.TextField(max_length=100, null=True, blank=True)
