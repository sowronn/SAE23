from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AeroportsForm(ModelForm):
    class Meta:
        model = models.Aeroports
        fields = ("id", "nom", "pays")
        labels = {
            "id" : _("numero de l'aeroport"),
            "nom" : _("nom de l'aeroport"),
            "pays" : _("pays de l'aeroport"),
        }

class PistesForm(ModelForm):
    class Meta:
        model = models.Pistes
        fields = ("numero", "aeroport", "longueur")
        labels = {
            "numero" : _("numero de piste"),
            "aeroport" : _("aeroport"),
            "longueur" : _("longueure de la piste"),
        }
class CompagniesForm(ModelForm):
    class Meta:
        model = models.Compagnies
        fields = ("id", "nom", "description", "pays_de_rattachement")
        labels = {
            "id" : _("numero de compagnie"),
            "nom" : _("nom de la compagnie"),
            "description" : _("description de la compagnie"),
            "pays_de_rattachement" : _("pays de d'origine de la compagnie"),
        }

class TypeavionForm(ModelForm):
    class Meta:
        model = models.Typeavions
        fields = ("id", "marque", "model", "description", "image", "longueurpistenecessaire")
        labels = {
            "id" : _("numero aeroport"),
            "marque" : _("marque de l'avion"),
            "model" : _("modele de l'avion"),
            "description" : _("Description de l'avion"),
            "image" : _("Airplane picture"),
            "longueurpistenecessaire" : _("longueur de piste"),
        }

class AvionsForm(ModelForm):
    class Meta:
        model = models.Avions
        fields = ("id", "nom", "compagnies", "model")
        labels = {
            "id" : _("numero d'avion"),
            "nom" : _("nom d'avion"),
            "compagnies" : _("nom de companie"),
            "model" : _("modele d'avions"),
        }

class VolsForm(ModelForm):
    class Meta:
        model = models.Vols
        fields = ("id", "avions", "pilote", "aeroport_de_depart", "date_de_depart", "heure_de_depart", "aeroport_de_darriver", "date_de_darriver", "heure_de_darriver")
        labels = {
            "id" : _("numero de vol"),
            "avions" : _("model d'avion"),
            "pilote" : _("nom et prenom du pilote"),
            "aeroport_de_depart" : _("nom de l'aeroport de depart"),
            "date_de_depart" : _("date du depart"),
            "heure_de_depart" : _("heur de depart"),
            "aeroport_de_darriver" : _("nom de l'aeroport d'arriver"),
            "date_de_darriver" : _("date d'arriver"),
            "heure_de_darriver" : _("heur d'arriver"),
        }