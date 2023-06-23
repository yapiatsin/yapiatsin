from django.urls import path
from .import views
from .views import MarqueListView, MarqueView


urlpatterns = [
    #--------------------------------home-----------------------------#
    path('', views.AccueilView.as_view(), name='accueil'),

    path('rien', views.RienView.as_view(), name='Rien'),

    
    #--------------------Authentication--------------------#
    #---------Authent_all----------#
    path('login', views.LoginView.as_view(), name='login'),
    path('404', views.Page404View.as_view(), name='404'),

    #---------Authent_admin---------#
    path('forgot_password', views.ForgetPasswordView.as_view(), name='forgot-password'),
    path('admin_register', views.AdminRegisterView.as_view(), name='Admin-register'),
    path('user_list', views.UserListeView.as_view(), name='user-list'),
   
    #--------------------------Admin Page-------------------#
    
    path('admin_page', views.AdminPageView.as_view(), name='admin-page'),

    #----------------------------projet------------------------#
    path('table_Projet', views.TableProjetView.as_view(), name='table-Projet'),
    path('add_proj', views.AddProjetView.as_view(), name='add-proj'),
    path('Imprime_list_proj', views.ImprimeListProjView.as_view(), name='Imprime-proj'),

    #-------------------------Extend base----------------------#
    path('baseadmin', views.BaseAdminView.as_view(), name='Base-admin'),
    path('baseUser', views.BaseUserView.as_view(), name='Base-user'),

    #-----------------------------Car--------------------------#
    
    path('delete_car', views.DeletCarView.as_view(), name='delete_car'),
    path('list_vehi_list', views.TabListCarView.as_view(), name='liste_véhi_list'),
    path('add_car', views.AddCarView.as_view(), name='add_car'),
    path('car/edit/<str:pk>', views.UpdateCarView.as_view(), name='update_car'),
    #path('car_detail/<str:pk>', views.CarDetailView.as_view(), name='detail_car'),
    path('car_detail', views.CarDetail, name='detail_car'),

    #-----------------------------marque--------------------------#
    path('add_marque/', views.AddMarqueView.as_view(), name='add_car_marque'),
    path('marque/<str:cats>/', MarqueView, name='marque'),
    path('marque-list/', MarqueListView, name='list_car_marque'),
    
     #-----------------------------Course--------------------------#
    path('add_course', views.AddCourseView.as_view(), name='add-course'),
    path('tab_course', views.TabCourseView.as_view(), name='tab-course'),
    path('imprime_course', views.ImprimeCourseView.as_view(), name='imprime-course'),

]




