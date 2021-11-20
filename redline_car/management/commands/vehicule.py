# -*- coding: utf-8 -*-
"""
Pour utiliser cette commande: python manage.py vehicule
"""
import csv
from django.core.management.base import BaseCommand
from catalogue.models import Categorie, Vehicule


class Command(BaseCommand):
    help = "Vide et enregistre la liste de véhicule du fichier CSV"

    def handle(self, *args, **options):

        CATEGORIE = Categorie.objects.all()
        CLEAR_VEHICULE = Vehicule.objects.all()
        CLEAR_VEHICULE.delete()

        with open("C:\Concession\\redline\catalogue\management\commands\\redline_db.csv", newline='') as f:
            spamReader = csv.reader(f, delimiter=',', quotechar='-')
            data = list(spamReader)
            for row in data[1:]:
                for cat in CATEGORIE:
                    if str(cat) == row[1]:
                        query = Vehicule(
                            nom=row[0],
                            categorie=cat,
                            prix=int(row[2])
                        )
                        query.save()
