from django.shortcuts import render
from app.models import Hyd_Jobs,Pune_Jobs,Bangalore_Jobs


def Hyd_jobs_view(request):
    hyd_jobs = Hyd_Jobs.objects.all()
    context={
        'hyd_jobs': hyd_jobs
    }
    return render(request,'hyd_jobs.html',context)

def Pune_jobs_view(request):
    hyd_jobs = Hyd_Jobs.objects.all()
    context={
        'Pune_jobs': hyd_jobs
    }
    return render(request,'Pune_jobs.html',context)


def Banglore_jobs_view(request):
    Banglore_jobs = Hyd_Jobs.objects.all()
    context={
        'Banglore_jobs': Banglore_jobs
    }
    return render(request,'Banglore_jobs.html',context)
