from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('time/' ,views.time_info_now)


]