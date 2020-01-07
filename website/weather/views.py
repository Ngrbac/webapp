from django.shortcuts import render
from django.views.generic import ListView
from .models import City


def weatherView(request):    
    return render(request, template_name='weather/base.html')

class WeatherListView(ListView):    
    model = City
    template_name = 'weather/weather.html'
    context_object_name = 'weather'