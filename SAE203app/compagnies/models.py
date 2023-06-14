from django.db import models

# Create your models here.


class compagnies(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    paysderatachement = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"la compagnie: {self.nom} description: {self.description} paysderatachement: {self.paysderatachement} ID: {self.id}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "description": self.description, "paysderatachement": self.paysderatachement, "id": self.id}
