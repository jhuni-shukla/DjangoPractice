from django.db import models

class Hyd_Jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.BigIntegerField()


class Bangalore_Jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.BigIntegerField()


class Pune_Jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.BigIntegerField()