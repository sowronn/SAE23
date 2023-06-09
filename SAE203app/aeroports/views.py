from django.shortcuts import render
from .forms import aeroportsForm

# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = aeroportsForm(request)
        return render(request, "aeroports/ajout.html", {"form": form})
    else :
        form = aeroportsForm()
        return render(request, "aeroports/ajout.html", {"form": form})

def traitement(request):
    lform = aeroportsForm(request.POST)
    if lform.is_valid():
        aeroports = lform.save()
        return render(request, "aeroports/traitement.html", {"aeroports" : aeroports})
    else :
        return render(request, "aeroports/ajout.html", {"form": lform})
