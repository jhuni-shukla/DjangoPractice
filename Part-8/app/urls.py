from django.urls import path
from app import views

urlpatterns=[
    path('index/',views.index_view),
    path('movies/',views.movies_view),
    path('sports/',views.sports_view),
    path('politics/',views.politics_view)
]