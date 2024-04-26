import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dataretriever2.settings')
import django
django.setup()

from app.models import Student
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)                #start from 6 and 9
    num=str(d1)                    #no added to string for concatination
    for i in range(9):             # 9 times loop will be executed
        num=num+str(randint(0,9))  #randon no from 0 to 9      
    return int(num) 
 
def populate(n):
    for i in range(n):
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1,max=100)
        femail=fake.email()
        fphonenumber=phonenumbergen()
        fadress=fake.address()
        student_record=Student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=fadress,)
n=int(input('Enter the number of Record'))
populate(1)
print(f'{n} records inserted successfully')
