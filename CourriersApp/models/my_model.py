from django.forms import ModelForm, Textarea
from django.db import models
from django import forms
import django_filters
from django.views.generic.list import ListView
#from CourriersApp.filters import CourrierFilter
# Create your models here.



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


"""class Bureau(models.Model):
    title = models.CharField(max_length=50)"""

class CourrierDepart(models.Model):
    num = models.PositiveIntegerField()
    date = models.DateField()
    date_emission = models.DateField()
    reference = models.TextField(blank = True)
    origine = models.CharField(max_length=100)
    objet = models.TextField(blank = True)
    bureau = models.CharField(max_length=100)

    #bureau = models.ForeignKey(Bureau,on_delete= models.CASCADE)

    class Meta:
        db_table= "courriersapp_courrierdepart"

class CourrierFilter(django_filters.FilterSet):
    class Meta:
        model = Courrier
        fields = '__all__'

class SearchView(ListView):
    model = Courrier
    template_name = 'search_crr.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Courrier.objects.filter(objet__contains=query)
            result= postresult
        else:
            result = None
        return result




    #bureau=models.ChoiceField(max_length=1, choices = BUREAU)

   #def __str__(self):
        #return self.reference


