from django.db import models

# Create your models here.
class compagnie(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pays = models.CharField(max_length=100)

