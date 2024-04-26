from django.shortcuts import render
from app.forms import StudentForm

def form_view(request):
    submitted=False
    sname=''
    # form = StudentForm()
    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            print('form validation is successfull and printing data')
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            sname=form.cleaned_data['name']
            submitted=True
    form = StudentForm()        
    return render(request, 'form.html', {'form':form,'submitted':submitted,'sname':sname})

    #empty form to display form to enduser
    #this form object contains end user provided data
    # form = StudentForm(request.POST)
    #from.cleaned_data['name]-the name entered by end user and cleaned_data : is dictionary which contains end user provided data
    #form.is_valid : to check validation are successful or not