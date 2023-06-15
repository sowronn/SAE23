from django.shortcuts import render, HttpResponseRedirect
from .forms import volsForm
from . import models

# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = volsForm(request)
        return render(request, "vols/ajout.html", {"form": form})
    else:
        form = volsForm()
        return render(request, "vols/ajout.html", {"form": form})


def traitement(request):
    lform = volsForm(request.POST)
    if lform.is_valid():
        vols = lform.save()
        return HttpResponseRedirect("/SAE203app")
    else:
        return render(request, "vols/ajout.html", {"form": lform})


def index(request):
    liste = list(models.vols.objects.all())
    return render(request, "vols/index.html", {"liste": liste})


def affiche(request, id):
    vols = models.vols.objects.get(pk=id)
    return render(request, "vols/affiche.html", {"vols": vols})


def update(request, id):
    vols = models.vols.objects.get(pk=id)
    form = volsForm(vols.dico())
    return render(request, "vols/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = volsForm(request.POST)
    if lform.is_valid():
        vols = lform.save(commit=False)
        vols.id = id
        vols.save()
        return HttpResponseRedirect("/SAE203app/")
    else:
        return render(request, "vols/update.html", {"form": lform, "id": id})


def delete(request, id):
    vols = models.vols.objects.get(pk=id)
    vols.delete()
    return HttpResponseRedirect("/SAE203app/")