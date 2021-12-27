
from django.urls import path
from . import views

urlpatterns = [
    path('film/', views.FormView.as_view()),
    path('parser/', views.ParserAnimeView.as_view()),
]    