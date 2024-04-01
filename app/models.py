from django.db import models
class Gender(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True,)
    phone = models.CharField(max_length=10,null=True,)
    gender = models.ForeignKey(Gender,on_delete=models.PROTECT,null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

