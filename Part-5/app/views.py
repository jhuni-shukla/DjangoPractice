from django.shortcuts import render
import datetime

# Create your views here.
def Welcome_Templates(request):
    return render(request,'apptemplates/index.html')

#template tags
def datetime_view(request):
    date=datetime.datetime.now()
    my_dict={'msg':date}
    #Various Alternative for writing dictionary
    return render(request,'apptemplates/date_time.html',{'msg':date})
    # return render(request,'apptemplates/date_time.html',my_dict)
    # return render(request,'apptemplates/date_time.html',context=my_dict)
