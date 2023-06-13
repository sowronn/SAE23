from django.shortcuts import render, HttpResponseRedirect
from .forms import aeroportsForm
from . import models

# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = aeroportsForm(request)
        return render(request, "aeroports/ajout.html", {"form": form})
    else:
        form = aeroportsForm()
        return render(request, "aeroports/ajout.html", {"form": form})


def traitement(request):
    lform = aeroportsForm(request.POST)
    if lform.is_valid():
        aeroports = lform.save()
        return HttpResponseRedirect("/SAE203app")
    else:
        return render(request, "aeroports/ajout.html", {"form": lform})


def index(request):
    liste = list(models.aeroports.objects.all())
    return render(request, "Aeroports/index.html", {"liste": liste})


def affiche(request, id):
    aeroports = models.aeroports.objects.get(pk=id)
    return render(request,"aeroport/affiche.html",{"aeroports": aeroports})


def update(request, id):
    aeroports = models.aeroports.objects.get(pk=id)
    form = aeroportsForm(aeroports.dico)
    return render(request, "aeroports/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = aeroportsForm(request.POST)
    if lform.is_valid():
        aeroports = lform.save(commit=False)
        aeroports.id = id
        aeroports.save()
        return HttpResponseRedirect("/SAE203app/")
    else:
        return render(request, "aeroports/update.html", {"form": lform, "id": id})