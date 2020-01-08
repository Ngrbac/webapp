from __future__ import absolute_import, unicode_literals
import bs4
import requests
from .models import City, CityData
from celery import Celery
from website.celery import app

@app.task(name='update')    
def weather_update():
    url = "https://vrijeme.hr/hrvatska1_n.xml"
    response = requests.request("GET", url).content
    soup = bs4.BeautifulSoup(response, 'lxml')
    cities = soup.select('grad')
    
    for city in cities:
        c = City.objects.create_city(
                city.gradime.contents[0],
                city.lat.contents[0],
                city.lon.contents[0])        
        d = CityData.objects.add_city_data(
                c,
                city.podatci.temp.contents[0],
                city.podatci.vlaga.contents[0],
                city.podatci.tlak.contents[0],
                city.podatci.tlaktend.contents[0],        
                city.podatci.vjetarsmjer.contents[0],
                city.podatci.vjetarbrzina.contents[0],
                city.podatci.vrijeme.contents[0],
                soup.datumtermin.datum.contents[0],
                soup.datumtermin.termin.contents[0],
            )