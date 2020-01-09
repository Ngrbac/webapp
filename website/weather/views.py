from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import City, CityData

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
    
class CityDataDetail(DetailView):
    model = CityData
    context_object_name = 'citydata'    