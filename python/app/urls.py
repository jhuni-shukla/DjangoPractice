from django.urls import path
from app import views

urlpatterns = [
    path('add',views.add_view),
]
