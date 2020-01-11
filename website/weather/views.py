from .models import City, CityData
from .serializers import  CityCleanSerializer, DataSerializer, CityDataSerializer
import requests
from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.generic import ListView
from django.views.generic.detail import DetailView

def weatherView(request):    
    return render(request, template_name='weather/base.html')

class CityListView(ListView):        
    model = City
    template_name = 'weather/cities.html'
    context_object_name = 'cities'
    paginate_by=9
    queryset = City.objects.all().order_by('gradime')    
    
class CityDetail(DetailView):
    model = City
    template_name = 'weather/citydetail.html'
    context_object_name = 'city'  

class CityList(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'citylist.html'
    
    def get(self, request):
        queryset = City.objects.all()
        serializer = CityCleanSerializer(queryset, many=True)
        return Response({'cities': serializer.data})

## api    
class DataView(viewsets.ModelViewSet):
    queryset = CityData.objects.all()
    serializer_class  = DataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)       
    
class CityDataView(viewsets.ModelViewSet):  
    queryset = City.objects.all()
    serializer_class  = CityDataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  
    
class CityCleanView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class  = CityCleanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)