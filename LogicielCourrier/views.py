from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    #return HttpResponse ('Logiciel gestion de courrier')
    return render(request, 'home.html')

def courrierA_view(request):
    #return HttpResponse ("Courrier Arrivés")
    return render(request, 'courrierArrives.html')

def courrierD_view(request):
    return render(request, 'courrierDepart.html')