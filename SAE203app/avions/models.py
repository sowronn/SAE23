from django.db import models

# Create your models here.

class avions(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    compagnie = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"l'avion: {self.nom} compagnie: {self.compagnie} modèle: {self.modele} ID: {self.id}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "compagnie": self.compagnie, "modele": self.modele, "id": self.id}
