from django.db import models
from django.contrib.auth.models import User
from user_management.models import Seller


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    poids = models.IntegerField()

    def __str__(self):
        return f"{self.nom, self.poids, self.id}"


class Vehicule(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE
    )
    prix = models.IntegerField(default=0)
    thumbnail = models.FilePathField()

    def __str__(self):
        return f"{self.nom, self.prix, self.categorie, self.thumbnail, self.id}"  # noqa


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    car = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    immat = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id, self.date, self.buyer, self.seller, self.car, self.immat}"  # noqa
