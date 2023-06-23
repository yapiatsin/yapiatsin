from django.contrib import admin

from .models import *

# Register your models here.

class AdminProjet(admin.ModelAdmin):
    search_fields =('name','date_deb','date_fin')
    model = Projet
    list_display = ('name','date_deb','date_fin')
    
class AdminVehicule(admin.ModelAdmin):
    search_fields =('immatriculation','marque','couleur','num_serie','vehi_image','prix', 'vehi_enregistre_date')
    model = Projet
    list_display = ('immatriculation','marque','couleur','num_serie','vehi_image','prix', 'vehi_enregistre_date')
    
class AdminMarque(admin.ModelAdmin):
    search_fields =('marque','logo')
    model = Marque
    list_display = ('marque','logo')
    


# Title et header du site admin
admin.site.site_header = 'PARC AUTOMOBILE'
admin.site.site_title = 'Parc ADMINISTRATION'

admin.site.register(Projet, AdminProjet)
admin.site.register(Marque, AdminMarque)
admin.site.register(Vehicule, AdminVehicule )










