from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
    age=forms.IntegerField()

#max_length is optional in forms.py    