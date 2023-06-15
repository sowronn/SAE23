from django.shortcuts import render, HttpResponseRedirect
from . forms import CompagniesForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = CompagniesForm(request)
        return render(request, "tourdecontrole/compagnies/formulaire.html", {"form": form})
    else:
        form = CompagniesForm()
        id = ""
        return render(request, "tourdecontrole/compagnies/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = CompagniesForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indexcompagnies/')
    else:
        return render(request, "tourdecontrole/compagnies/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Compagnies.objects.all())
    return render(request, 'tourdecontrole/compagnies/index.html', {'liste': liste})


def affiche(request, id):
    compagnies = models.Compagnies.objects.get(pk=id)
    return render(request, 'tourdecontrole/compagnies/affiche.html', {"compagnies": compagnies})


def update(request, id):
    compagnies = models.Compagnies.objects.get(pk=id)
    form = CompagniesForm(compagnies.dico())
    return render(request, 'tourdecontrole/compagnies/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = CompagniesForm(request.POST)
    if lform.is_valid():
        compagnies = lform.save(commit=False)
        compagnies.id = id
        compagnies.save()
        return HttpResponseRedirect('/indexcompagnies/')
    else:
        return render(request, "tourdecontrole/compagnies/update.html", {"form": lform, "id": id})


def delete(request, id):
    compagnies = models.Compagnies.objects.get(pk=id)
    compagnies.delete()
    return HttpResponseRedirect('/aeroports/indexcompagnies/')