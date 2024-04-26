from django.shortcuts import render
import datetime
import random

# Create your views here.
def Course_info(request):
    time = datetime.datetime.now()
    name='Django'
    prerequirred='Python'
    my_dict={'time':time,'name':name,'prerequirred':prerequirred}
    return render(request,'courses.html',context=my_dict)


def astro_talk(request):
    msg_list=[
        'Very Soon,You are going to get married to a beautuiful lady',
        'The Golden Days ahead',
        'Have a Good Day and Achieve your dream',
        'Dont Forget to Learn Django'
    ]
    names_list=['Jhuni','Avni','Adarsh','Ayush','Prakash']
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h<12:
        s = 'Good Morning'
    else:
        s='Good Day'    
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict={'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'astro_msg.html',my_dict)
