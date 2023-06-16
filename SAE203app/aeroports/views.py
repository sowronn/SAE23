from django.shortcuts import render, HttpResponseRedirect
from . forms import AeroportsForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = AeroportsForm(request)
        return render(request, "tourdecontrole/aeroport/formulaire.html", {"form": form})
    else:
        form = AeroportsForm()
        id = ""
        return render(request, "tourdecontrole/aeroport/formulaire.html", {"form": form, "id": id})

def traitement(request):
    lform = AeroportsForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indexaeroport/')
    else:
        return render(request, "tourdecontrole/aeroport/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Aeroports.objects.all())
    return render(request, 'tourdecontrole/aeroport/index.html', {'liste': liste})


def affiche(request, id):
    aeroport = models.Aeroports.objects.get(pk=id)
    return render(request, 'tourdecontrole/aeroport/affiche.html', {"aeroport": aeroport})


def update(request, id):
    aeroport = models.Aeroports.objects.get(pk=id)
    form = AeroportsForm(aeroport.dico())
    return render(request, 'tourdecontrole/aeroport/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = AeroportsForm(request.POST)
    if lform.is_valid():
        aeroport = lform.save(commit=False)
        aeroport.id = id
        aeroport.save()
        return HttpResponseRedirect('/indexaeroport/')
    else:
        return render(request, "tourdecontrole/aeroport/update.html", {"form": lform, "id": id})


def delete(request, id):
    aeroports = models.Aeroports.objects.get(pk=id)
    aeroports.delete()
    return render(request, "tourdecontrole/aeroport/index.html")
