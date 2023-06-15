from django.shortcuts import render, HttpResponseRedirect
from . forms import AvionsForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = AvionsForm(request)
        return render(request, "tourdecontrole/avions/formulaire.html", {"form": form})
    else:
        form = AvionsForm()
        id = ""
        return render(request, "tourdecontrole/avions/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = AvionsForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indexavions/')
    else:
        return render(request, "tourdecontrole/avions/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Avions.objects.all())
    return render(request, 'tourdecontrole/avions/index.html', {'liste': liste})


def affiche(request, id):
    avions = models.Avions.objects.get(pk=id)
    return render(request, 'tourdecontrole/avions/affiche.html', {"avions": avions})


def update(request, id):
    avions = models.Avions.objects.get(pk=id)
    form = AvionsForm(avions.dico())
    return render(request, 'tourdecontrole/avions/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = AvionsForm(request.POST)
    if lform.is_valid():
        avions = lform.save(commit=False)
        avions.id = id
        avions.save()
        return HttpResponseRedirect('/indexavions/')
    else:
        return render(request, "tourdecontrole/avions/update.html", {"form": lform, "id": id})


def delete(request, id):
    avions = models.Avions.objects.get(pk=id)
    avions.delete()
    return HttpResponseRedirect('/aeroports/indexavions/')