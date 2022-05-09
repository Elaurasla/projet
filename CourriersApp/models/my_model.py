from django.forms import ModelForm, Textarea
from django.db import models
from django import forms
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django.forms.widgets import RadioSelect ,CheckboxSelectMultiple

# Create your models here.
BUREAU = models.CharField(('FI','FINANCES'),('PE','PESE'),('CO','CONTENTIEUX'),('BR','BRH'))


class Courrier(models.Model):
    num = models.PositiveIntegerField()
    date = models.DateField()
    date_emission = models.DateField()
    reference = models.TextField(blank = True)
    origine = models.CharField(max_length=100)
    objet = models.TextField(blank = True)
    bureau = models.CharField(max_length=100)

class Meta:
    db_table = "courriers"

    #bureau=models.ChoiceField(max_length=1, choices = BUREAU)

   # def __str__(self):
        #return self.reference


