from rest_framework import serializers
from .models import City, CityData

#odabir polja koja će sadržavati JSON na API endpointu
   
class DataSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = CityData
        fields = ('id', 'url', 'temper', 'tlak', 'tlaktend', 'vlaga', 'vjetarsmjer', 'vjetarbrzina', 'datum', 'sat', 'grad')
        
class CityCleanSerializer(serializers.ModelSerializer):    
    class Meta:
        model = City
        fields = ('id', 'gradime')
        
class CityDataSerializer(serializers.HyperlinkedModelSerializer):
    citydata_set = DataSerializer(many=True, read_only=True)    
    class Meta:
        model = City
        fields = ('id', 'url', 'gradime', 'lat', 'lon', 'citydata_set')
        
