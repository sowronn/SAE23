from django.shortcuts import render, HttpResponseRedirect
from .forms import pistesForm
from . import models

# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = pistesForm(request)
        return render(request, "pistes/ajout.html", {"form": form})
    else:
        form = pistesForm()
        return render(request, "pistes/ajout.html", {"form": form})


def traitement(request):
    lform = pistesForm(request.POST)
    if lform.is_valid():
        pistes = lform.save()
        return HttpResponseRedirect("/SAE203app")
    else:
        return render(request, "pistes/ajout.html", {"form": lform})


def index(request):
    liste = list(models.pistes.objects.all())
    return render(request, "pistes/index.html", {"liste": liste})


def affiche(request, id):
    pistes = models.pistes.objects.get(pk=id)
    return render(request,"aeroport/affiche.html",{"pistes": pistes})


def update(request, id):
    pistes = models.pistes.objects.get(pk=id)
    form = pistesForm(pistes.dico())
    return render(request, "pistes/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = pistesForm(request.POST)
    if lform.is_valid():
        pistes = lform.save(commit=False)
        pistes.id = id
        pistes.save()
        return HttpResponseRedirect("/SAE203app/")
    else:
        return render(request, "pistes/update.html", {"form": lform, "id": id})


def delete(request, id):
    pistes = models.pistes.objects.get(pk=id)
    pistes.delete()
    return HttpResponseRedirect("/SAE203app/")