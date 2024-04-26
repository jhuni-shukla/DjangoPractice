# from random import randint
# from faker import Faker

# fakegen = Faker()
# name=fakegen.name()

# print(name)


# fakegen = Faker()
# for i in range(10):
#     name=fakegen.name()
#     print(name)

# fakegen = Faker()
# for i in range(10):
#     fname=fakegen.first_name()
#     print(fname)

# date=fakegen.date()
# print(date)

# number=fakegen.random_number(5)
# print(number)

# email=fakegen.email()
# print(email)

# phone_number=fakegen.phone_number()
# print(phone_number)

# city=fakegen.city()
# print(city)

# state=fakegen.state()
# print(state)

# print(fakegen.random_int(min=0, max=9999))

# print(fakegen.random_element(elements=('Project Manager','Team Manager','Software')))
                             

from faker import Faker
from random import *
fakegen=Faker()
def phonenumbergen():
    d1=randint(6,9)                #start from 6 and 9
    num=str(d1)                 #no added to string for concatination
    for i in range(9):             # 9 times loop will be executed
        num=num+str(randint(0,9))  #randon no from 0 to 9      
    return int(num) 
 
def populate(n):
    for i in range(n):
        frollno = fakegen.random_int(min=1, max=999)
        fname = fakegen.name()
        fdob = fakegen.date()
        fmarks = fakegen.random_int(min=1, max=100)
        femail = fakegen.email()
        fphonenumber = phonenumbergen()
        fadress = fakegen.address()
        student_record = {
            'rollno': frollno,
            'name': fname,
            'dob': fdob,
            'marks': fmarks,
            'email': femail,
            'phonenumber': fphonenumber,
            'address': fadress
        }
        Student.objects.get_or_create(student_record )
populate(1)                              