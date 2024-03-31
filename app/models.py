from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5)
    age = models.IntegerField()
