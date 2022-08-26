# -*- coding: utf-8 -*-
"""
Pour utiliser cette commande: python manage.py vehicule
"""
import csv
import os

from django.core.management.base import BaseCommand
from redline_car.models import Categorie, Vehicule


class Command(BaseCommand):
    help = "Vide et enregistre la liste de véhicule du fichier CSV"

    def handle(self, *args, **options):

        CATEGORIE = Categorie.objects.all()
        CLEAR_VEHICULE = Vehicule.objects.all()
        CLEAR_VEHICULE.delete()
        db_file = os.path.join(
            os.path.abspath(
                os.path.dirname('manage.py')),
            'redline_car/management/commands/redline_db.csv'
        )

        with open(
                db_file,
                newline='',
        ) as f:
            spamreader = csv.reader(
                f,
                delimiter=',',
                quotechar='-'
            )
            data = list(spamreader)
            for row in data[1:]:
                for cat in CATEGORIE:
                    if str(cat.nom) == row[1]:
                        photo_name = row[0].replace(" ", "_")
                        query = Vehicule(
                            nom=row[0],
                            categorie=cat,
                            prix=int(row[2]),
                            thumbnail=f"redline_car/assets/catalogue/"
                                      f"{cat.nom}/{photo_name}.jpg"
                        )
                        print(query)
                        query.save()
