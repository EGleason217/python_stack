from django.db import models

class Wizard(models.Model):
    name = models.CharField(max_length=225)
    house = models.CharField(max_length=225)
    pet = models.CharField(max_length=225)
    year = models.IntegerField()