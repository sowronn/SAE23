from django.db import models

# Create your models here.
class Aeroports(models.Model):
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"l'aéroport {self.nom} situé {self.pays}, ayant l'id: {self.id}."
        return chaine

    def dico(self):
        return {"nom":self.nom, "pays":self.pays, "id":self.id}

class Pistes(models.Model):
    numero = models.IntegerField(blank = False)
    aeroport = models.CharField(max_length=100)
    longueur = models.IntegerField(blank = False)

    def __str__(self):
        chaine = f"La piste d'atterissage n° {self.numero} del'aéroport {self.aeroport} a une longueur de  {self.longueur} mètres."
        return chaine

    def dico(self):
        return {"id":self.id,"numero":self.numero, "aeroport":self.aeroport, "plongueur":self.longueur}

class Compagnies(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    pays_de_rattachement = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.description}. Le pays rattaché a cette compagnie est {self.pays_de_rattachement}."
        return chaine

    def dico(self):
        return {"nom":self.nom,"description":self.description, "pays_de_rattachement":self.pays_de_rattachement}

class Typeavions(models.Model):
    marque = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to = "image")
    longueurpistenecessaire = models.IntegerField(blank = False)


    def __str__(self):
        chaine = f"L'avion {self.model} de la marque {self.marque}, est {self.description}, ayant besoin d'une piste d'une longueur de {self.longueurpistenecessaire} metre de long."
        return chaine

    def dico(self):
        return {"model":self.model, "marque":self.marque, "description":self.description, "longueurpistenecessaire":self.longueurpistenecessaire}

class Avions(models.Model):
    nom = models.CharField(max_length=100)
    compagnies = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"L'avion {self.id} de la compagnie {self.compagnies}, est un {self.nom}{self.model}."
        return chaine

    def dico(self):
        return {"is":self.id, "nom":self.nom, "compagnies":self.compagnies, "model":self.model}

class Vols(models.Model):
    avions = models.ForeignKey(Avions, on_delete = models.CASCADE)
    pilote = models.CharField(max_length=100)
    aeroport_de_depart = models.ForeignKey(Aeroports, on_delete = models.CASCADE, related_name = "Aeroport_Depart")
    aeroport_de_darriver = models.ForeignKey(Aeroports, on_delete = models.CASCADE, related_name = "Aeroport_Arrivee")
    date_de_depart = models.DateField(null=True, blank=True)
    date_de_darriver = models.DateField(null=True, blank=True)
    heure_de_depart = models.TimeField(auto_now=False, auto_now_add=False)
    heure_de_darriver = models.TimeField(auto_now=False, auto_now_add=False)



    def __str__(self):
        chaine = f"Le vol numero {self.id} avec l'avion {self.avions}, le pilote {self.pilote}, décollera a {self.heure_de_depart} le {self.date_de_depart} a l'aeroport {self.aeroport_de_depart}. Le vol atterrira a {self.heure_de_darriver}, le {self.date_de_darriver}, a l'aeroport {self.aeroport_de_darriver}."
        return chaine

    def dico(self):
        return {"id":self.id, "avions":self.avions, "pilote":self.pilote, "heure_de_depart":self.heure_de_depart, "date_de_depart":self.date_de_depart, "aeroport_de_depart":self.aeroport_de_depart, "heure_de_darriver":self.heure_de_darriver, "date_de_darriver":self.date_de_darriver, "aeroport_de_darriver":self.aeroport_de_darriver}
