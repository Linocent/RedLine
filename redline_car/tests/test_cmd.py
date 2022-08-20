from django.test import TestCase
from django.core.management import call_command
from redline_car.models import (
    Categorie,
    Vehicule,
)


class CategoryTest(TestCase):
    def test_category_cmd(self):
        call_command('category')
        self.assertEqual(Categorie.objects.count(), 16)


class VehiculeTest(TestCase):
    def test_vehicule_cmd(self):
        call_command('vehicule')
        self.assertEqual(Vehicule.objects.count(), 386)
