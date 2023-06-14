from django.db import models

# Create your models here.

class pistes(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero = models.CharField(max_length=100)
    longueur = models.CharField(max_length=100)
    aeroport = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"piste : {self.numero} de l'aéroport: {self.aeroport} de longueur: {self.longueur} d'ID: {self.id}"
        return chaine

    def dico(self):
        return {"numero": self.numero, "aeroport": self.aeroport, "longueur": self.longueur, "id": self.id}
