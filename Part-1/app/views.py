from django.shortcuts import HttpResponse
import datetime

# Create your views here.
def time_info_now(request):
    time=datetime.datetime.now()
    s = '<h1>Current Date and Time : '+str(time)+' </h1>'
    return HttpResponse(s)