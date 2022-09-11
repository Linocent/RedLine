from django.test import TestCase
from django.core.management import call_command
from redline_car.models import (
    Categorie,
    Vehicule,
)


class CategoryTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(
            id=1,
            nom='cat_to_remove',
            poids='10',
        )
        self.categorie.save()

    def test_remove_old_entry(self):
        call_command('category')
        self.assertFalse(
            Categorie.objects.filter(
                nom__icontains='cat_to_remove'
            ))

    def test_category_cmd(self):
        call_command('category')
        self.assertEqual(Categorie.objects.count(), 16)


class VehiculeTest(TestCase):
    def setUp(self):
        call_command('category')

        self.vehicule = Vehicule.objects.create(
            id=1,
            nom='vehicule_to_remove',
            categorie=Categorie.objects.get(nom__icontains='Moto'),
            prix='10000',
            thumbnail='img/thumbnail.jpg'
        )
        self.vehicule.save()

    def test_remove_old_entry(self):
        call_command('vehicule')
        self.assertFalse(
            Vehicule.objects.filter(
                nom__icontains='vehicule_to_remove'
            ))

    def test_vehicule_cmd(self):
        call_command('vehicule')
        self.assertEqual(Vehicule.objects.count(), 380)

