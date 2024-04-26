from django.shortcuts import render
from app.forms import FeedBackForm

def Feedback_view(request):
    form = FeedBackForm()
    submitted = False
    sname=''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Feedback sucessfully submitted')
            print('#'*30)
            print('name:',form.cleaned_data['name'])
            print('email:',form.cleaned_data['email'])
            print('rollno:',form.cleaned_data['rollno'])
            print('feedback:',form.cleaned_data['feedback'])
            submitted=True   
            sname = form.cleaned_data['name'] 
        else:
            print('some field validation failed')    
    
    return render(request, 'feedback.html',{'form':form,'submitted':submitted,'sname':sname})
