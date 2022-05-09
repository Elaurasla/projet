from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
from CourriersApp.models.my_model import Courrier

class CourrierForm(forms.ModelForm):
    class Meta:
        model = models.my_model.Courrier
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']
        
        #fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']
