from django.db import models


# Create your models here.
class Logindb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Number = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Password = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Profile Image", null=True, blank=True)


class itemdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile Image", null=True, blank=True)

class divisiondb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    subName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile Image", null=True, blank=True)


class Productdb(models.Model):
    subName=models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.EmailField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField()
    Description = models.TextField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile Image", null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class Orderdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.TextField(max_length=100, null=True, blank=True)




