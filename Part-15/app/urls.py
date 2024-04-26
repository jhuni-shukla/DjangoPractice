from django.urls import path
from app import views

urlpatterns = [
    path('feedback',views.Feedback_view),
]
