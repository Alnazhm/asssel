from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
