from django.db import models


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    poids = models.IntegerField()

    def __str__(self):
        return f"{self.nom, self.poids, self.id}"


class Vehicule(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.IntegerField(default=0)
    thumbnail = models.FilePathField()

    def __str__(self):
        return f"{self.nom, self.prix, self.categorie, self.thumbnail, self.id}"
