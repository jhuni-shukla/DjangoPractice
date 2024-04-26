from django.http import HttpResponse

def test_view2(request):
    msg='<h1>Hello APP2</h1>'
    return HttpResponse(msg)
