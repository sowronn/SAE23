from django.shortcuts import render, HttpResponseRedirect
from .forms import compagniesForm
from . import models

# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = compagniesForm(request)
        return render(request, "compagnies/ajout.html", {"form": form})
    else:
        form = compagniesForm()
        return render(request, "compagnies/ajout.html", {"form": form})


def traitement(request):
    lform = compagniesForm(request.POST)
    if lform.is_valid():
        compagnies = lform.save()
        return HttpResponseRedirect("/SAE203app")
    else:
        return render(request, "compagnies/ajout.html", {"form": lform})


def index(request):
    liste = list(models.compagnies.objects.all())
    return render(request, "compagnies/index.html", {"liste": liste})


def affiche(request, id):
    compagnies = models.compagnies.objects.get(pk=id)
    return render(request,"compagnies/affiche.html",{"compagnies": compagnies})


def update(request, id):
    compagnies = models.compagnies.objects.get(pk=id)
    form = compagniesForm(compagnies.dico())
    return render(request, "compagnies/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = compagniesForm(request.POST)
    if lform.is_valid():
        compagnies = lform.save(commit=False)
        compagnies.id = id
        compagnies.save()
        return HttpResponseRedirect("/SAE203app/")
    else:
        return render(request, "compagnies/update.html", {"form": lform, "id": id})


def delete(request, id):
    compagnies = models.compagnies.objects.get(pk=id)
    compagnies.delete()
    return HttpResponseRedirect("/SAE203app/")