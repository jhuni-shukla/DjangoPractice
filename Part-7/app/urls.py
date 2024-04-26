from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('news/',views.News_Page),
    path('movies/',views.movies_view),
    path('sports/',views.sports_view),
    path('politics/',views.politics_view)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)