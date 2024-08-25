from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class PredefinedCity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
