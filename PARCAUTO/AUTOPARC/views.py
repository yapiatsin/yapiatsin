from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .forms import *


# Create your views here.

#-----------------Pour les tests--------------#
class RienView(View):

    templates_name = 'table/table_cars.html'
    Projets = Projet.objects.all()
    context = {
        'Projets': Projets
    }

    def get(self,request, *args, **kwargs):
        return render(request, self.templates_name, self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request, self.templates_name, self.context)

#-----------------Accueil--------------
class AccueilView(View):
    template_name = 'accueil.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request, *args, **kwargs):

        return render(request, self.template_name)
    

#------------------------------Authentication-----------------------#   
class LoginView(View):

    templates_name = 'authentication/login.html'
    
    def get(self,request, *args, **kwargs):
        return render(request, self.templates_name)
    
    def post(self,request, *args, **kwargs):
        return render(request, self.templates_name)
    
class AdminPageView(View):
    templates_name = 'admin_pages/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)

    
class AdminRegisterView(View):
    templates_name = 'authentication/register.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


class ForgetPasswordView(View):
    templates_name = 'authentication/forgot_password.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    
class UserListeView(View):
    templates_name = 'authentication/user_liste.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    
class Page404View(View):
    templates_name = 'admin_pages/404.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


#---------------------------projet------------------------#
class AddProjetView(View):
    template_name = 'formulaire/add_proj.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request, *args, **kwargs):

        data = {
            'name': request.POST.get('name'),
            'date_fin': request.POST.get('date_fin'),
        }
        try:
            if created := Projet.objects.create(**data):
                messages.success(request, "Enregistrement effectuée")
            else:
                messages.error(request, 'Desolé, vérifier vos donnée')

        except Exception as e:  
            messages.error(request, f"Sorry our system is detecting the following issues {e}.")
        return render(request, self.template_name)
    
class TableProjetView(View):
    template_name = 'table/tables_projet.html'
    Projets = Projet.objects.all()
    context = {
        'Projets': Projets
    }

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name, self.context)

  
class ImprimeListProjView(View):
    template_name = 'imprime/Imprime_list_proj.html'
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name)

#------------------------------Base Extends-----------------------#   
#-----------Folder Admin-----------#
class BaseAdminView(View):
    templates_name = 'admin_pages/Base_admin.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)

class BaseUserView(View):
    templates_name = 'admin_pages/Base_user.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)
    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name)


#------------------------------Car-----------------------#   
class AddCarView(CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = 'formulaire/add_car.html'
    success_url = reverse_lazy('admin-page') 

    
class DeletCarView(ListView):
    model = Vehicule
    template_name = 'table/Table_car_delete.html'
    
    
class TabListCarView(ListView):
    model = Vehicule
    template_name = 'table/table_cars_liste.html'

class UpdateCarView(UpdateView):
    form_class =EditCarForm
    model = Vehicule
    template_name = 'table/update_car.html'
    success_url = reverse_lazy('liste_véhi_list')

#class CarDetailView(DetailView):
#    model = Vehicule
#    template_name = 'table/car_detail.html'

def CarDetail(request):
    return render (request,'table/car_detail.html',{})
#------------------------------Marque-----------------------#   

class AddMarqueView(CreateView):
    model = Marque
    form_class = MarqueForm
    template_name = 'formulaire/add_car_marque.html'
    success_url = reverse_lazy('admin-page') 

def MarqueListView(request):
    marq_menu_list = Marque.objects.all()
    return render(request, 'table/marques_list.html' ,{'marq_menu_list': marq_menu_list})

def MarqueView(request, cats):
    marque_vehicule = Vehicule.objects.filter(marque=cats)
    return render(request, 'table/marques.html', {'cats':cats, 'marque_vehicule':marque_vehicule})

#------------------------------Course-----------------------# 
class AddCourseView(View):
    template_name = 'formulaire/add_cours.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name)
    

class TabCourseView(View):
    template_name = 'table/table_course.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
class ImprimeCourseView(View):
    template_name = 'imprime/Imprime_list_course.html'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name)
    





