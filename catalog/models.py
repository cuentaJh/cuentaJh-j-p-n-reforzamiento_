from django.db import models

# Create your models here.

class Catalog(models.Model):
    nombre = models.CharField(max_length=25)
    pais = models.CharField(max_length=27, default = '')
    edad = models.IntegerField()
