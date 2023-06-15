from django.db import models

# Create your models here.

class vols(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    avions = models.ForeignKey(avions, on_delete=models.CASCADE)
    pilote = models.CharField(max_length=100)
    aeroport_de_depart = models.ForeignKey(aeroports, on_delete=models.CASCADE, related_name="Aeroport_Depart")
    aeroport_de_darriver = models.ForeignKey(aeroports, on_delete=models.CASCADE, related_name="Aeroport_Arrivee")
    date_de_depart = models.DateField(null=True, blank=True)
    date_de_darriver = models.DateField(null=True, blank=True)
    heure_de_depart = models.TimeField(auto_now=False, auto_now_add=False)
    heure_de_darriver = models.TimeField(auto_now=False, auto_now_add=False)


def __str__(self):
    chaine = f"Flight number {self.id} with the plane {self.avions} with the pilot {self.pilote}, will take off at {self.heure_de_depart} the {self.date_de_depart} at {self.aeroport_de_depart}. The flight and will arrive at its destination at {self.heure_de_darriver}, the {self.date_de_darriver}, at {self.aeroport_de_darriver}."
    return chaine


def dico(self):
    return {"id": self.id, "avions": self.avions, "pilote": self.pilote, "heure_de_depart": self.heure_de_depart,
            "date_de_depart": self.date_de_depart, "aeroport_de_depart": self.aeroport_de_depart,
            "heure_de_darriver": self.heure_de_darriver, "date_de_darriver": self.date_de_darriver,
            "aeroport_de_darriver": self.aeroport_de_darriver}