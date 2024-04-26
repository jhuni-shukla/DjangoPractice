from django.shortcuts import HttpResponse

def add_view(request):
    a=2
    b=4
    c=request.GET.get('c',None)

    try:
        if c is not None:
            return HttpResponse("Helo world")
        else:
            return HttpResponse("Error")
    except Exception as e:
            return HttpResponse(e)

