from django.contrib import admin
from django.urls import path
from comptes.views import signup
from LogicielCourrier.views import home_view
from LogicielCourrier import settings 
from CourriersApp import views

from comptes.views import logout_user
from comptes.views import signup_page

from CourriersApp.views import index
from CourriersApp.views import crr 
from CourriersApp.views import view 
from CourriersApp.views import delete  
from CourriersApp.views import update  

#from CourriersApp.views import edit  
from CourriersApp.views import search_posts  


from django.urls import reverse_lazy



from . import views
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', signup, name="signup"),
    path('', views.home_view, name='home'),
    path('courrierA/',views.courrierA_view, name='courrier_arrive' ),
    path('courrierD/',views.courrierD_view ),
    path('logout/', logout_user, name='logout'),
    path('connexion/', views.connexion, name='connexion'),
    path('signup/', signup_page, name='inscriptionn'),
    path('courriervue/', index, name='vue_courrier'),
    path('crr/', crr, name="crr"), 
    path('view/', view, name="vue"),
    path('delete/<int:id>', delete),
    path('update/<str:id>', update, name='modifier'),
    #path('edit/<int:id>', edit),
    path('search_crr/', search_posts, name='search_crr'),

]

  