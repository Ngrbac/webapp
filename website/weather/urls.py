from django.urls import path, include
from django.conf.urls import url
from .views import weatherView, CityListView, CityDetail, CityCleanView, DataView, CityDataView, CityList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cities', CityCleanView, 'cities')
router.register('citydata', CityDataView, 'citydata')
router.register('data', DataView, 'data')

urlpatterns = [
    path('', weatherView, name = 'home'),
    path('api/', include(router.urls)),
    path('cities2/', CityList.as_view(), name = 'cities2'),  
    path('cities/', CityListView.as_view(), name = 'cities'),    
    path('cities/<int:pk>/', CityDetail.as_view(), name='city-detail'),    
    ]
