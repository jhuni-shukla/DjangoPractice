from django.urls import path
from app import views

urlpatterns = [
    path('student',views.Student_view)
]
