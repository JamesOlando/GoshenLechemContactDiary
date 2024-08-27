from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Diary(models.Model):
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    dateofbirth = models.CharField(max_length=100)
    companyofoperation = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)