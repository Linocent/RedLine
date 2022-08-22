# -*- coding: utf-8 -*-
"""
Pour utiliser cette commande: python manage.py category
"""
import csv
import os.path

from django.core.management.base import BaseCommand
from redline_car.models import Categorie


class Command(BaseCommand):
    help = "Vide et enregistre les catagories du fichier CSV"

    def handle(self, *args, **options):
        clear_cat = Categorie.objects.all()
        clear_cat.delete()
        db_file = os.path.join(
            os.path.abspath(
                os.path.dirname('manage.py')
            ),
            'redline_car/management/commands/redline_db_categorie.csv'
        )

        with open(
                db_file,
                newline=''
        ) as f:
            spamreader = csv.reader(
                f,
                delimiter=',',
                quotechar='-'
            )
            data = list(spamreader)
            for row in data[1:]:
                query = Categorie(
                    nom=row[0],
                    poids=row[1],
                )
                print(row[0])
                query.save()
