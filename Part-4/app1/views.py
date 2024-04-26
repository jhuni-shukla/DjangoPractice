from django.http import HttpResponse

def test_view1(request):
    msg='<h1>Hello APP1</h1>'
    return HttpResponse(msg)
