from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename = models.CharField(max_length=30)
    eage = models.IntegerField()
    esalary = models.FloatField()
    edate_of_joining = models.DateField()
    eadress = models.CharField(max_length=300)

    def __str__(self):
        return self.ename