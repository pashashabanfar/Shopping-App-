from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    salary = models.FloatField()
    email = models.CharField(max_length=35)