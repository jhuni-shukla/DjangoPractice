from django.contrib import admin
from app.models import Hyd_Jobs,Pune_Jobs,Bangalore_Jobs

class Hyd_JobAdmin(admin.ModelAdmin):
    list_display = ['date','company']
admin.site.register(Hyd_Jobs,Hyd_JobAdmin)

class Pune_JobAdmin(admin.ModelAdmin):
    list_display = ['date','company']
admin.site.register(Pune_Jobs,Pune_JobAdmin)

class Bangalore_JobsAdmin(admin.ModelAdmin):
    list_display = ['date','company']
admin.site.register(Bangalore_Jobs,Bangalore_JobsAdmin)
