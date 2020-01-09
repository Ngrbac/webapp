from django.db import models
import datetime

class CityManager(models.Manager):    
    def create_city(self, gradime, lat, lon):
        try:        
            if self.get_city(gradime):
                return self.get_city(gradime).first()
            else:
                city = City.objects.create(gradime=gradime, lat=lat, lon=lon)
                return city
        except:
            with open('log.txt', 'a') as file:
                file.write(f'{datetime.datetime.now}: failed city add.')
        
    def get_city(self, gradime):
        return City.objects.filter(gradime=gradime)

class CityDataManager(models.Manager):    
    def add_city_data(self, grad, temper, vlaga, tlak, tlaktend, vjetarsmjer, vjetarbrzina, vrijeme, datum, sat):
        try:
            if tlak[-1] == '*':
                tlak = float(tlak[:-1])
            else: 
                pass
            
            if tlak == '-':
                    tlak = 0
            else:
                pass            
            
            if temper[0] == '-':
                    temper = -float(temper[1:])
            else:
                pass
            
            if vjetarbrzina == '-':
                vjetarbrzina = 99.9
            
            if tlaktend == '-':
                tlaktend = 99.9
            elif tlaktend[0] == '+' or tlaktend[0] == '-':
                if tlaktend[0] == '-':
                    tlaktend = -float(tlaktend[1:])
                else:
                    tlaktend = float(tlaktend[1:])
            else:
                pass
            
            city_data = self.create(grad=grad, temper=temper, vlaga=vlaga, tlak=tlak, tlaktend=tlaktend, 
                                    vjetarsmjer=vjetarsmjer, vjetarbrzina=vjetarbrzina, vrijeme=vrijeme, datum=datum, sat=sat)
            #return city_data
        except:
            with open('log.txt', 'a') as file:
                file.write(f'{datetime.datetime.now}: failed update. \n')
            pass
    
class City(models.Model):
    gradime = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=5, decimal_places=3)
    lon = models.DecimalField(max_digits=5, decimal_places=3)   
    
    def create(self, gradime, lat, lon):
        self.gradime = gradime
        self.lat = lat
        self.lon = lon
        return self

    objects = CityManager()
    
class CityData(models.Model):
    grad = models.ForeignKey(City, on_delete=models.CASCADE)
    temper = models.DecimalField(max_digits=5, decimal_places=2)
    vlaga = models.IntegerField(3)
    tlak = models.DecimalField(max_digits=5, decimal_places=1)
    tlaktend = models.DecimalField(max_digits=3, decimal_places=1)
    vjetarsmjer = models.CharField(max_length=2)
    vjetarbrzina = models.DecimalField(max_digits=3, decimal_places=1)
    vrijeme = models.CharField(max_length=50)
    datum = models.DateField(auto_now=True)
    sat = models.IntegerField(2)
    
    objects = CityDataManager()