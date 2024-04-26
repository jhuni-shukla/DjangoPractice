from django.shortcuts import HttpResponse


def Hyderabad_Job_Search(request):
    s="Hello, world. You're at the Hyderabad Job Search"
    return HttpResponse("<h1>Hello, world. You're at the Hyderabad Job Search <h1>")


def Pune_Job_Search(request):
    s="Hello, world. You're at the Pune Job Search"
    return HttpResponse("<h1>Hello, world. You're at the Hyderabad Job Search <h1>")


def Jaipur_Job_Search(request):
    s="Hello, world. You're at the Jaipur Job Search"
    return HttpResponse("<h1>Hello, world. You're at the Hyderabad Job Search <h1>")

