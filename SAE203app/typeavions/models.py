from django.db import models

# Create your models here.

class typeavions(models.Model):
    id = models.BigAutoField(primary_key=True)
    marque = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    modele = models.CharField(max_length=100)
    longueur_piste = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images_upload/')

    def __str__(self):
        chaine = f"l'avion: {self.modele} marque: {self.marque} descrption: {self.description} longueur de piste necessaire: {self.longueur_piste} image: {self.image}ID: {self.id}"
        return chaine

    def dico(self):
        return {"model": self.modele, "marque": self.marque, "description": self.description, "longueur_piste": self.longueur_piste, "image": self.image, "id": self.id}
