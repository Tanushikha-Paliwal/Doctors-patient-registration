from django.db import models


# Create your models here.

GENDER_CHOICE = (("F", "FEMALE"), ("M", "MALE"))


class Doctors(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()
    degree = models.CharField(max_length=300)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    reports = models.FileField(upload_to="reports")
    gender = models.CharField(choices=GENDER_CHOICE, max_length=8)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    message = models.TextField()
    