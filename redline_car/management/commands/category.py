# -*- coding: utf-8 -*-
"""
Pour utiliser cette commande: python manage.py category
"""
import csv
from django.core.management.base import BaseCommand
from redline_car.models import Categorie


class Command(BaseCommand):
    help = "Vide et enregistre les catagories du fichier CSV"

    def handle(self, *args, **options):
        clear_cat = Categorie.objects.all()
        clear_cat.delete()
        with open(
                "/home/le_shtroumpf/OC/RedLine//redline_car/"
                "management/commands/redline_db_categorie.csv",
                newline=''
        ) as f:
            spamReader = csv.reader(
                f,
                delimiter=',',
                quotechar='-'
            )
            data = list(spamReader)
            for row in data[1:]:
                query = Categorie(
                    nom=row[0],
                    poids=row[1],
                )
                query.save()
