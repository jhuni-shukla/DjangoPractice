from django.shortcuts import render
from app.models import Employee_IS

def empdata_view(request):
    emp_list = Employee_IS.objects.all()
    #print(emp_list)
    context = {
        'emp_list': emp_list,
    }
    return render(request, 'empdata.html',context)
