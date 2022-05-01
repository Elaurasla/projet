from django.contrib import admin
from django.urls import path
from comptes.views import signup
from LogicielCourrier.views import home_view
from LogicielCourrier import settings 

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', signup, name="signup"),
    path('', views.home_view, name='home'),
    path('courrierA/',views.courrierA_view ),
    path('courrierD/',views.courrierD_view ),

]
