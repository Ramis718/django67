
from django.urls import path
from . import views

urlpatterns = [
    path('film/', views.AnimeView.as_view(), name='1+1'),
    path('parser/', views.ParserAnimeView.as_view(), name='parser'),
]    