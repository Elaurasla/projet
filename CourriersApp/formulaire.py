from django import forms
from django.forms import ModelForm
from CourriersApp.models import my_model
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django.forms.widgets import RadioSelect ,CheckboxSelectMultiple


BUREAU =[('FI','FINANCES'),('PE','PESE'),('CO','CONTENTIEUX'),('BR','BRH'),]


class CourrierForm(ModelForm):
    class Meta:
        model = my_model.Courrier
        bureau = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BUREAU,
    )
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']


        #fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']


#from students.models.my_model import Courrier
 
class CourrierDepartForm(ModelForm):
    class Meta:
        model = my_model.Courrier
        fields = ['num', 'date', 'date_emission', 'reference', 'origine', 'objet','bureau']