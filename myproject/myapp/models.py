from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    salary = models.FloatField()
    email = models.CharField(max_length=35)


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username
