from django.contrib import admin
from app.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','rollno']

admin.site.register(Student,StudentAdmin)