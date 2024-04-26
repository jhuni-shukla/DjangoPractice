from django.contrib import admin
from app.models import Employee_IS

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['ename', 'edept']

admin.site.register(Employee_IS,EmployeeAdmin)
