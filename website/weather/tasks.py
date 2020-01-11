from __future__ import absolute_import, unicode_literals
import bs4          #za scraping podataka
import requests     #za dohvat xmla
from .models import City, CityData
from celery import Celery   #za asinkrono obavljanje zadataka
from website.celery import app
import datetime     #prilagođavanje formata datuma

#dohvat podataka za bazu o vremenu
@app.task(name='update')    
def weather_update():    
    url = "https://vrijeme.hr/hrvatska1_n.xml"
    response = requests.request("GET", url).content
    soup = bs4.BeautifulSoup(response, 'lxml')
    cities = soup.select('grad')
    
    #vrijeme sa xmla
    date = datetime.datetime.strptime(soup.datumtermin.datum.contents[0], '%d.%m.%Y').strftime('%Y-%m-%d')
    time = soup.datumtermin.termin.contents[0]
    
    #provjera postoji li zapis istog termina
    if CityData.objects.filter(datum=date,sat=time):
        return '\n Data already exists. Trying again later.'        #string kao status info o celery zadatku
    else:             
        for city in cities:
            #manager prvo provjeri ima li grad, ako ne doda ga
            c = City.objects.create_city(
                    city.gradime.contents[0],
                    city.lat.contents[0],
                    city.lon.contents[0]
                    )    
            #dodavanje novih podataka    
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
        return '\n Data update started.'    #string kao status info o celery zadatku
        