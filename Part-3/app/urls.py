from django.urls import path
from app import views

urlpatterns = [
    path('time/',views.Greeting_Message_info)
]
