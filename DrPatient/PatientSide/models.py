from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    age = models.IntegerField()