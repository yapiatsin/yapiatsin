from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Marque(models.Model):
    marque = models.CharField(max_length= 225)
    logo = models.ImageField(null=True, blank=True, upload_to="marques/")
    
    def __str__(self):
        return {self.marque},{self.logo}
    def get_absolute_url(self):
        return reverse('liste_véhi_list')


class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100)
    carburant = models.CharField(max_length=100)
    vehi_image = models.ImageField(null=True, blank=True, upload_to="images/")
    prix = models.IntegerField(default=0)
    date_achat = models.DateTimeField()
    garentie = models.DateTimeField()
    vehi_enregistre_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.marque 



    
#----------------Projet-----------------#
class Projet(models.Model):
    name = models.CharField(max_length=50)
    date_deb = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=False, blank=True)
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
    def __str__(self):
        return f'{self.name}{self.date_deb}{self.date_fin}'





class Carburant(models.Model):

    STATION_TYPE=(('TOTAL','TOTAL'),
                  ('SHELL','SHELL'),
                  ('DHL','DHL'),
                  ('PETRO IVOIRE','PETRO IVOIRE'),
                  ('IVOIRE WIN','IVOIRE WIN'),
                  )

    #type_intervention = models.ForeignKey(Intervention, null=True, on_delete=models.CASCADE, related_name = "Interv_carbur")
    #vehicule = models.ForeignKey(Car, null=True, on_delete=models.CASCADE )
    date_prise = models.DateTimeField(auto_now_add=True)  
    kilometrage_dern_plein = models.IntegerField(null=True,blank=True)
    kilometrage_actu = models.IntegerField(null=True,blank=True)   
    volume = models.DecimalField(max_digits=1000, decimal_places=2)
    cout = models.DecimalField(max_digits=1000, decimal_places=2)
    
    
    station = models.CharField(max_length=13,choices=STATION_TYPE)
    #reçu = models.ImageField(null=True, blank=True, upload_to = 'image') 
    def __str__(self) :
        return f"{self.date_prise}{self.kilometrage_dern_plein}{self.kilometrage_actu}{self.station}{self.volume}{self.cout}"




























































