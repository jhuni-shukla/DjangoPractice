from django.urls import path
from app import views
from app.models import Employee_IS

urlpatterns = [
    path('empdata',views.empdata_view)
]
