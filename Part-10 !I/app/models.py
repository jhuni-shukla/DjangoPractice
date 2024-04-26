from django.db import models

# Create your models here.
class Employee_IS(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    edept = models.CharField(max_length=100)
    ephone = models.IntegerField()
    eemail = models.CharField(max_length=100)
    eaddress = models.CharField(max_length=100)
    esalary = models.IntegerField()
