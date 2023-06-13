from django.db import models

# Create your models here.

class aeroports(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"l'aeroport: {self.nom} dans le pays: {self.pays} d'ID: {self.id}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "pays": self.pays, "id": self.id}