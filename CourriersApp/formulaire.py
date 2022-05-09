from django import forms
from django.forms import ModelForm
from CourriersApp.models import my_model

class CourrierForm(ModelForm):
    class Meta:
        model = my_model.Courrier
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']
        #fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']


#from students.models.my_model import Courrier
 