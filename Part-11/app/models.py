from django.db import models

class Student(models.Model):
    rollno=models.IntegerField()
    name = models.CharField(max_length=100)
    dob = models.DateField()
    marks = models.IntegerField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField(15)
    address=models.CharField(max_length=100)
