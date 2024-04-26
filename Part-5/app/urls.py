from django.urls import path
from app import views

urlpatterns = [
    path("welcome/",views.Welcome_Templates),
    path("time/",views.datetime_view)
]
