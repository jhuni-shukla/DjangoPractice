from django.shortcuts import render
from app.models import Student

def Student_view(request):
    student_list = Student.objects.all()
    #student_list = Student.objects.filter(marks__lt=25)
    #student_list = Student.objects.filter(name_startswith='A')
    #student_list = Student.objects.all().order_by('marks')
    #student_list = Student.objects.all().order_by('-marks')
    context = {
       'student_list': student_list,
    }
    return render(request,'student.html',context)

# Create your views here.
