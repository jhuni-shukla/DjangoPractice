from django.shortcuts import HttpResponse
from django.shortcuts import render
import datetime

def Greeting_Message_info(request):
    date= datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = '<h1>Hello Friend,'
    if h<12:
        msg = msg+'Good Morning'
    elif h<16:
        msg = msg+'Good Afternoon'
    elif h<24:
        msg = msg+'Good Evening'
    else:
        msg = msg+'Good Night'
    msg = msg+'</h1><hr>'  
    msg = msg+'<h1>Now Server time is: '+str(date)+' </h1>'       
    print(msg)
    return HttpResponse(msg)