from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    message = models.TextField()
    password = models.CharField(max_length=255)