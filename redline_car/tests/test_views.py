import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from redline_car.models import (
    Categorie,
    Vehicule,
    Sales,
)
from user_management.models import Discord, Seller


class IndexPageTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(
            id=1,
            nom='Compact',
            poids='10',
        )
        self.categorie.save()

        self.vehicule = Vehicule.objects.create(
            id=1,
            nom='Blista',
            categorie=self.categorie,
            prix='10000',
            thumbnail='img/thumbnail.jpg'
        )
        self.vehicule.save()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redline_car/index.html')

    def test_query(self):
        response = self.client.post(
            '/redline/',
            data={'query': 'Blista'}
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/?query=Blista')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/?query=no_vehicule')
        self.assertTemplateUsed(response, 'redline_car/404.html')
        self.assertEqual(
            response.context['message'],
            'Aucun résultat trouvé pour no_vehicule.'
        )


class SeachPageTest(TestCase):
    def setUp(self):
        categorie = Categorie.objects.create(
            id=1,
            nom='Compact',
            poids='10',
        )
        categorie.save()

        self.vehicule = Vehicule.objects.create(
            id=1,
            nom='Blista',
            categorie=categorie,
            prix='10000',
            thumbnail='img/thumbnail.jpg'
        )
        self.vehicule.save()

    def test_search_page(self):
        response = self.client.get(reverse(
            'search',
            kwargs={'category_id': '1'}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redline_car/search.html')
        vehicule = Vehicule.objects.all()
        self.assertEqual(str(response.context['answer']), str(vehicule))
        response = self.client.get('/redline/search/2/')
        self.assertEqual(response.status_code, 200)


class DetailPageTest(TestCase):
    def setUp(self):
        categorie = Categorie.objects.create(
            id=1,
            nom='Compact',
            poids='10',
        )
        categorie.save()

        vehicule = Vehicule.objects.create(
            id=1,
            nom='Blista',
            categorie=categorie,
            prix='10000',
            thumbnail='img/thumbnail.jpg'
        )
        vehicule.save()

    def test_detail_page(self):
        response = self.client.get(reverse(
            'details',
            kwargs={'vehicule_id': '1'}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redline_car/detail.html')


class VehiculePageTest(TestCase):
    def setUp(self):
        cat1 = Categorie.objects.create(
            id=1,
            nom='Compact',
            poids='10',
            )
        cat1.save()

        cat2 = Categorie.objects.create(
            id=2,
            nom='Compact',
            poids='10',
            )
        cat2.save()

    def test_dvehicule_page(self):
        response = self.client.get(reverse('vehicule'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redline_car/vehicule.html')
        categories = Categorie.objects.all()
        self.assertEqual(str(response.context['category']), str(categories))


class OrderPageTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="123456789",
        )
        self.client.login(username='test@test.com', password='123456789')

        categorie = Categorie.objects.create(
            id=1,
            nom='Compact',
            poids='10',
        )
        categorie.save()

        vehicule = Vehicule.objects.create(
            id=1,
            nom='Blista',
            categorie=categorie,
            prix='10000',
            thumbnail='img/thumbnail.jpg'
        )
        vehicule.save()
        discord = Discord.objects.create(
            discord_id='test#1452',
            user=user,
        )
        discord.save()

    def test_order_page(self):
        response = self.client.post(reverse('order'), data={'vehicule_id': 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.client.logout()
        response = self.client.post(reverse('order'), data={'vehicule_id': 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/user_management/log_in/?next=/redline/order/'
        )


class AccountPageTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='user_1',
            email='user1@test.com',
            password='123456789',
        )

        seller = User.objects.create_user(
            username='user_2',
            email='user2@test.com',
            password='123456789',
        )
        seller.save()

        category = Categorie.objects.create(
            id=1,
            nom='Compact',
            poids='10',
            )
        category.save()

        vehicule = Vehicule.objects.create(
            id=1,
            nom='Blista',
            categorie=category,
            prix='10000',
            thumbnail='img/thumbnail.jpg'
        )
        vehicule.save()

        user_seller = Seller.objects.create(
            id=1,
            seller=seller,
        )
        seller.save()

        sales = Sales.objects.create(
            id=1,
            date=datetime.date,
            buyer=user,
            seller=user_seller,
            car=vehicule,
            immat='123aze56',
        )
        sales.save()

    def test_account_page(self):
        self.client.login(username='user1@test.com', password='123456789')
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redline_car/my_account.html')
        car_bought = Sales.objects.all()
        self.assertEqual(str(response.context['car_bought']), str(car_bought))
        self.client.logout()
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/user_management/log_in/?next=/redline/my_account/'
        )


class LegalMentionPageTest(TestCase):
    def test_legal_mention(self):
        response = self.client.get(reverse('legal_mention'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redline_car/legal_mention.html')
