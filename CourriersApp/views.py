from django.shortcuts import render, redirect
from .formulaire import CourrierForm
from .models.my_model import Courrier

from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from CourriersApp import models
#from CourriersApp.models import my_model
from django.http import HttpResponse
from django.template import loader

from .filters import CourrierFilter



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
            try:
                form.save()
                return redirect ('/view')
            except: 
                pass
    else:
        form = CourrierForm()
    return render(request, 'index_test.html', {'form': form})

def view(request):
    courriers = Courrier.objects.all()
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
    return render(request, 'index_test.html', context)

"""def edit(request, id):
    courriers = Courrier.objects.get(id=id)
    return render(request, "edit.html", {'courriers':courriers})"""


"""
def courrier_filtre(request,id):
    courrier= Courrier.objects.get(id=id)
    ordre = courrier.order_set.all()
    ordre_count = ordre.count()
    myFilter = OrderFilter()
    context = {'courier': courrier, 'ordre': ordre, 'ordre_count': ordre_count, 'myFilter': myFilter}
    return render(request, 'view.html', context)



@login_required
def courrier_list(request, *args, **kwargs):
    courriers = Courrier.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            courriers = Courrier.objects.filter(name__icontains=objet)

    context = {
        'courriers':courriers,
    } 

    return render(request, 'view.html', context)"""

@login_required
def search_posts(request):
    search = request.GET.get('search')
    courriers = Courrier.objects.filter(objet=search)

    context = {
        'courriers':courriers
    }
    return render(request, 'search_crr.html', {'search': search})