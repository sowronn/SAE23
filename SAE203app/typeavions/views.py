from django.shortcuts import render, HttpResponseRedirect
from .forms import typeavionsForm
from . import models

# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = typeavionsForm(request)
        return render(request, "typeavions/ajout.html", {"form": form})
    else:
        form = typeavionsForm()
        return render(request, "typeavions/ajout.html", {"form": form})


def traitement(request):
    lform = typeavionsForm(request.POST)
    if lform.is_valid():
        typeavions = lform.save()
        return HttpResponseRedirect("/SAE203app")
    else:
        return render(request, "typeavions/ajout.html", {"form": lform})


def index(request):
    liste = list(models.typeavions.objects.all())
    return render(request, "typeavions/index.html", {"liste": liste})


def affiche(request, id):
    typeavions = models.typeavions.objects.get(pk=id)
    return render(request, "typeavions/affiche.html", {"typeavions": typeavions})


def update(request, id):
    typeavions = models.typeavions.objects.get(pk=id)
    form = typeavionsForm(typeavions.dico())
    return render(request, "typeavions/update.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = typeavionsForm(request.POST)
    if lform.is_valid():
        typeavions = lform.save(commit=False)
        typeavions.id = id
        typeavions.save()
        return HttpResponseRedirect("/SAE203app/")
    else:
        return render(request, "typeavions/update.html", {"form": lform, "id": id})


def delete(request, id):
    typeavions = models.typeavions.objects.get(pk=id)
    typeavions.delete()
    return HttpResponseRedirect("/SAE203app/")