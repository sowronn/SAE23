from django.shortcuts import render, HttpResponseRedirect
from .forms import avionsForm
from . import models

# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = avionsForm(request)
        return render(request, "avions/ajout.html", {"form": form})
    else:
        form = avionsForm()
        return render(request, "avions/ajout.html", {"form": form})


def traitement(request):
    lform = avionsForm(request.POST)
    if lform.is_valid():
        avions = lform.save()
        return HttpResponseRedirect("/SAE203app")
    else:
        return render(request, "avions/ajout.html", {"form": lform})


def index(request):
    liste = list(models.avions.objects.all())
    return render(request, "avions/index.html", {"liste": liste})


def affiche(request, id):
    avions = models.avions.objects.get(pk=id)
    return render(request, "avions/affiche.html", {"avions": avions})


def update(request, id):
    avions = models.avions.objects.get(pk=id)
    form = avionsForm(avions.dico())
    return render(request, "avions/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = avionsForm(request.POST)
    if lform.is_valid():
        avions = lform.save(commit=False)
        avions.id = id
        avions.save()
        return HttpResponseRedirect("/SAE203app/")
    else:
        return render(request, "avions/update.html", {"form": lform, "id": id})


def delete(request, id):
    avions = models.avions.objects.get(pk=id)
    avions.delete()
    return HttpResponseRedirect("/SAE203app/")