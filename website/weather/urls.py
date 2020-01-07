from django.urls import path
from .views import WeatherListView
from . import views

urlpatterns = [
    path('', views.weatherView, name = 'home'),
    path('weather/', WeatherListView.as_view(), name = 'weather'),    
]