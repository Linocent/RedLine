from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nom}"


class Vehicule(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom, self.prix}"