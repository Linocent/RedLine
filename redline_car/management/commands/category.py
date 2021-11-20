# -*- coding: utf-8 -*-
"""
Pour utiliser cette commande: python manage.py category
"""
import csv
from django.core.management.base import BaseCommand
from catalogue.models import Categorie


class Command(BaseCommand):
    help = "Vide et enregistre les catagories du fichier CSV"

    def handle(self, *args, **options):
        with open("C:\Concession\\redline\catalogue\management\commands\\redline_db_categorie.csv", newline='') as f:
            spamReader = csv.reader(f, delimiter=',', quotechar='-')
            data = list(spamReader)
            for row in data[1:]:
                query = Categorie(
                    nom=row[0]
                )
                query.save()
