from django import forms
from .models import *



choices = Marque.objects.all().values_list('marque','marque')
choices_list=[]

for item in choices:
    choices_list.append(item)
class VehiculeForm(forms.ModelForm):
    class Meta :
        model = Vehicule
        fields = ('immatriculation','marque','couleur','num_serie','carburant','vehi_image','prix','date_achat','garentie')

        widgets = {
            'immatriculation' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Immat...'}),
            'marque' : forms.Select( choices=choices_list ,attrs={'class': 'form-control'}),
            #'author' : forms.Select(attrs={'class': 'form-control'}),
            'couleur' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Couleur...'}),
            'num_serie' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'numero serie...'}),
            'carburant' : forms.TextInput(attrs={'class': 'form-control'}),
            'prix' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'prix...'}),
            'date_achat' : forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'garentie' : forms.SelectDateWidget(attrs={'class': 'form-control'}),

        }

class EditCarForm(forms.ModelForm):
    class Meta :
        model = Vehicule
        fields = '__all__'
        widgets = {
            'marque' : forms.TextInput(attrs={'class': 'form-control'}),
            'immatriculation' : forms.TextInput(attrs={'class': 'form-control'}),
            'marque' : forms.Select( choices=choices_list ,attrs={'class': 'form-control'}),
            #'author' : forms.Select(attrs={'class': 'form-control'}),
            'couleur' : forms.TextInput(attrs={'class': 'form-control'}),
            'num_serie' : forms.TextInput(attrs={'class': 'form-control'}),
            'carburant' : forms.TextInput(attrs={'class': 'form-control'}),
            'prix' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_achat' : forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'garentie' : forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }


class MarqueForm(forms.ModelForm):
    class Meta :
        model = Marque
        fields = '__all__'
        widgets = {
            'marque' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'marque...'}),
        }  



