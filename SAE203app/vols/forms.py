from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class avionsForm(ModelForm):
    model = models.vols
    fields = (
    "id", "avions", "pilote", "aeroport_de_depart", "date_de_depart", "heure_de_depart", "aeroport_de_darriver",
    "date_de_darriver", "heure_de_darriver")
    labels = {
        "id": _("Flight number"),
        "avions": _("Aircraft model"),
        "pilote": _("Driver's first and last name"),
        "aeroport_de_depart": _("Departure airport name"),
        "date_de_depart": _("Date of departure"),
        "heure_de_depart": _("Departure time"),
        "aeroport_de_darriver": _("Arrival airport name"),
        "date_de_darriver": _("Arrival date"),
        "heure_de_darriver": _("Arriving time"),
    }