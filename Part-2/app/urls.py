from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("hyd/",views.Hyderabad_Job_Search),
    path("pune/",views.Pune_Job_Search),
    path("jaipur/",views.Jaipur_Job_Search),
    
]
