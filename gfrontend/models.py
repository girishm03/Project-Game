from django.db import models

# Create your models here.

class ContactDB(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)

class registerDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    Game_name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)
