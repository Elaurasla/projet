from django.forms import ModelForm, Textarea
from django.db import models
from django import forms
import django_filters
from django.views.generic.list import ListView
from django.db.models import Q
#from CourriersApp.filters import CourrierFilter
# Create your models here.

class Courrier(models.Model):
    num = models.PositiveIntegerField()
    date = models.DateField()
    date_emission = models.DateField()
    reference = models.TextField(blank = True)
    origine = models.CharField(max_length=100)
    objet = models.TextField(blank = True)
    bureau = models.TextField(max_length=100)
    class Meta:
        db_table = "courriers"

class CourrierDepart(models.Model):
    num = models.PositiveIntegerField()
    date = models.DateField()
    date_emission = models.DateField()
    reference = models.TextField(blank = True)
    origine = models.CharField(max_length=100)
    objet = models.TextField(blank = True)
    bureau = models.TextField(max_length=100)
    class Meta:
        db_table = "courriersdepart"

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
            postresult = Courrier.objects.filter(origine__iexact=query)
            result = postresult
        else:
            result = None
        return result

  

class SearchView_objet(ListView):
    model = Courrier
    template_name = 'search_objet.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView_objet, self).get_queryset()
        query = self.request.GET.get('search_objet')
        if query:
            postresult = Courrier.objects.filter(objet__iexact=query) 
            result = postresult
        else:
            result = None 
        return result




"""
class SearchView(ListView):
    model = Courrier
    template_name = 'search_crr.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Courrier.objects.filter(objet__iexact=query)
            result= postresult
        else:
            result = None
        return result"""


#postresult = Courrier.objects.filter(Q(objet__iexact=query) & Q(origine__iexact=query))
