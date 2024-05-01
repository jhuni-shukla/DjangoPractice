#VALIDATORS BY CODERS - form empty after submit nothing data printed in console
# from django import forms

# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     rollno=forms.IntegerField()
#     feedback=forms.CharField(widget=forms.Textarea)
#     def clean_name(self):
#         print('validating name field only')
#         inputname = self.cleaned_data['name']
#         if len(inputname) < 4:
#             raise forms.ValidationError("Name must be atleast 4 characters")
#         return inputname
#     def clean_email(self):
#         print('validating email field only')
#         inputemail = self.cleaned_data['email']
#         return inputemail
#     def clean_rollno(self):
#         print('validating rollno field only')
#         inputrollno = self.cleaned_data['rollno']
#         return inputrollno

#FOR INBUILT VALIDATORS : 
#from django import forms    
#from django.core import validators

# class FeedBackForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # rollno=forms.IntegerField()
    # feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])


#CUSTOM VALIDATORS BY CODERS :
# def starts_with_d(value):
#      print('validating name field only start with d')
#     if value[0].lower()!= 'd':
#         raise forms.ValidationError("Name must start with D or d")
#     return value 
# def gmail_validators(value):
#     print('validating email field only gmail')
#     if '@gmail.com' not in value:
#         raise forms.ValidationError("Email must be gmail")
#     return value
# def gmail_validators(value):
#     if value[-10]!='@gmail.com':
#         raise forms.ValidationError("Email extension must be gmail")

# class FeedBackForm(forms.Form):
    # name = forms.CharField(validators=[starts_with_d])
    # email = forms.EmailField(validators=[gmail_validators])
    # rollno=forms.IntegerField()
    # feedback=forms.CharField(widget=forms.Textarea)
    

# SINGLE clean method validation
# from django import forms

# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     rollno=forms.IntegerField()
#     password=forms.CharField(widget=forms.PasswordInput)
#     feedback=forms.CharField(widget=forms.Textarea)  
    

#     def clean(self):
#         print('total form validations........')
#         total_cleaned_data = super().clean()
#         inputname=total_cleaned_data['name']
#         if inputname[0].lower() != 'd':
#             raise forms.ValidationError('Name should start with d')
#         inputmails = total_cleaned_data['email'] 
#         print('validationing email........')   
#         if inputmails[-10] != '@gmail.com':
#             raise forms.ValidationError('Email extension must be gmail')


#password and reenter password same
from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    rollno=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput) 
    feedback=forms.CharField(widget=forms.Textarea) 
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)  
    
    def clean(self):
            total_cleaned_data = super().clean()
            pwd = total_cleaned_data['password']
            rpwd = total_cleaned_data['rpassword']
            if pwd != rpwd:
                raise forms.ValidationError('Password must be same')
            bot_handler_value=total_cleaned_data['bot_handler']
            if len(bot_handler_value) > 0:
                 raise forms.ValidationError('This is a bot')