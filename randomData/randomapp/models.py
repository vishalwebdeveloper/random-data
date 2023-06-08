from django.db import models

# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=100)

class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class record(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
