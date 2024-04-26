from django.urls import path
from app import views

urlpatterns=[
    path("info",views.Course_info),
    path('astro',views.astro_talk)
]