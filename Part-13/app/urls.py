from django.urls import path
from app import views

urlpatterns = [
    path("hyd/",views.Hyd_jobs_view),
    path("pune/",views.Pune_jobs_view),
    path("banglore/",views.Banglore_jobs_view)
]
