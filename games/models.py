from django.db import models

# Create your models here.
class catdb(models.Model):
    C_name = models.CharField(max_length=100, null=True, blank=True)
    C_image = models.ImageField(upload_to="CIMAGE", null=True, blank=True)

class gamedb(models.Model):
    Category_name = models.CharField(max_length=100, null=True, blank=True)
    game_name = models.CharField(max_length=100, null=True, blank=True)
    game_desciption = models.CharField(max_length=100, null=True, blank=True)
    game_price = models.IntegerField(null=True, blank=True)
    game_image = models.ImageField(upload_to="GIMAGE", null=True, blank=True)