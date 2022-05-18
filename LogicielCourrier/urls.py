from django.contrib import admin
from django.urls import path, include
from comptes.views import connexion
from LogicielCourrier.views import home_view
from LogicielCourrier import settings 
from CourriersApp import views

from comptes.views import logout_user
from comptes.views import inscription

from CourriersApp.views import index

from CourriersApp.views import crr 
from CourriersApp.views import view 
from CourriersApp.views import delete  
from CourriersApp.views import update  

from CourriersApp.views import crr_depart
from CourriersApp.views import view_depart 
from CourriersApp.views import delete_depart 
from CourriersApp.views import update_depart


#from CourriersApp.views import courrierd_delete 
#from CourriersApp.views import courrierd_form  
#from CourriersApp.views import showlist  


from CourriersApp.models.my_model import SearchView
from CourriersApp.models.my_model import SearchView_objet
from django.urls import reverse_lazy

from . import views
   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', inscription, name="inscription"),
    path('', views.home_view, name='home'),
    path('courrierA/',views.courrierA_view, name='courrier_arrive' ),
    path('courrierD/',views.courrierD_view, name='courrier_depart' ),
    path('logout/', logout_user, name='logout'),
    path('connexion/', connexion, name='connexion'),

    path('courriervue/', index, name='vue_courrier'),

    path('crr/', crr, name="crr"), 
    path('view/', view, name="vue"),
    path('delete/<int:id>', delete), 
    path('update/<str:id>', update, name='modifier'),

    path('crrd/', crr_depart, name="crrd"), 
    path('viewd/', view_depart, name="vued"),
    path('deleted/<int:id>', delete_depart), 
    path('updated/<str:id>', update_depart, name='modifierd'),

    path('results/', SearchView.as_view(), name='search'),
    path('results_objet/', SearchView_objet.as_view(), name='search_objet'),


    #path('courrierd_form/',courrierd_form, name="courrierd"),

    #path('showlist/', showlist, name= 'showlist'),


]

  