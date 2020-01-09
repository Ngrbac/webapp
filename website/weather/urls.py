from django.urls import path
from .views import CityListView, CityDetail
from . import views

urlpatterns = [
    path('', views.weatherView, name = 'home'),
    path('cities/', CityListView.as_view(), name = 'cities'),    
    path('city/<int:pk>/', CityDetail.as_view(), name='city-detail'),
]