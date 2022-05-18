from django.shortcuts import render, redirect
from .formulaire import CourrierForm
from .formulaire import CourrierDepartForm

from .models.my_model import Courrier
from .models.my_model import CourrierDepart
from .models.my_model import CourrierFilter

from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from CourriersApp import models
#from CourriersApp.models import my_model
from django.http import HttpResponse
from django.template import loader


#from django.db import my_model
#from .models.my_model import Courrier

def index(request): 
    if request.method == "POST":
        form= CourrierForm(request.POST).save()
        return redirect('/courrier_arrive')
    form = CourrierForm()
    return render(request, 'index.html', {'form': form, 'dataCourriers':Courrier.objects.all()})

def crr(request):
    if request.method == "POST":
        form = CourrierForm(request.POST)
        if form.is_valid():
            bureau = form.cleaned_data.get('bureau')
            try:
                form.save()
                return redirect ('/crr')
            except:  
                pass
    else: 
        form = CourrierForm()
    return render(request, 'enregistrement_courrier.html', {'form': form})


def view(request):
    courriers = Courrier.objects.all().order_by('-id')
    return render(request, "view.html", {'courriers':courriers})


def delete(request, id):
    courriers= Courrier.objects.get(id=id)
    courriers.delete()
    return redirect("/view")


def update(request,id):
    courrier= Courrier.objects.get(id=id)
    form= CourrierForm(instance = courrier)
    if request.method == "POST":
        form = CourrierForm(request_POST, instance= courrier)
        if form.is_valid():
            form.save()
            return redirect('/view')
    context = {'form': form}
    return render(request, 'update.html', context)

def crr_depart(request):
    if request.method == "POST":
        form = CourrierDepartForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect ('/crrd')
            except:  
                pass
    else: 
        form = CourrierDepartForm()
    return render(request, 'courrierD_enregistrement.html', {'form': form})


def view_depart(request):
    courriersdepart = CourrierDepart.objects.all().order_by('-id')
    return render(request, "viewdepart.html", {'courriersdepart':courriersdepart})

def delete_depart(request, id):
    courriersdepart= CourrierDepart.objects.get(id=id)
    courriersdepart.delete()
    return redirect("/viewd")


def update_depart(request,id):
    courrierdepart= CourrierDepart.objects.get(id=id)
    form = CourrierDepartForm(instance = courrierdepart)
    if request.method == "POST":
        form = CourrierDepartForm(request_POST, instance= courrierdepart)
        if form.is_valid():
            form.save()
            return redirect('/viewd')
    context = {'form': form}
    return render(request, 'courrierd_form.html', context)


"""
@login_required
def search_posts(request):
    search = request.GET.get('search')
    courriers = Courrier.objects.filter(objet=search)

    context = {
        'courriers':courriers
    }
    return render(request, 'search_crr.html', {'search': search})
"""


"""
def courrierd_form(request):
    form = CourrierDepartForm()
    return render(request, 'courrierd_form.html',{'form':form})

def courrierd_delete(request):
    return"""

"""
def showlist(request):
    results= Courrier.objects.all
    return render(request, "enregistrement_courrier.html",{"showcity":results})"""

"""
def choice(request):
    courrier = Courrier.object.all()
    context = {'courrier': courrier}
    return render(request, "enregistrement_courrier.html", context)"""

"""
def choice(request):
    courrier = Courrier.objects.all()
    choix_bureau = ["finance", "brh", "contentieux", "logistique", "magasin","immo",'traitements']
    liste = []
    [liste.append(courrier[i].choix_bureau) for i in range(len(courrier))]
    return render(request, 'enregistrement_courrier.html', {"choix_bureau":choix_bureau,"courrier":courrier})
"""


