from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from redline_car.models import (
    Categorie,
    Vehicule,
    Sales,
)
from user_management.models import Discord, Seller


class SignUpTest(TestCase):
    def test_signup(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_management/signup.html')
        response = self.client.post(
            '/user_management/sign_up/',
            {
                'password1': '1234azerty56789',
                'password2': '1234azerty56789',
                'email': 'usertest@test.com',
                'first_name': 'first_name',
                'last_name': 'last_name',
                'discord_id': 'discord_id#1452',
            }
        )
        print(response.context)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user_management/log_in/')
        user = User.objects.count()
        self.assertEqual(user, 1)
        login = self.client.post(
            reverse('log_in'),
            data={
                'email': 'usertest@test.com',
                'password': '1234azerty56789',
            },
        )
        self.assertTrue(login)
        self.assertEqual(login.status_code, 302)


class LogInTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='test',
            email='test@test.com',
            password='12456789',
        )

    def test_sign_in(self):
        response = self.client.get(reverse('log_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_management/login.html')
        response = self.client.post(
            reverse('log_in'),
            data={
                'email': 'test@test.com',
                'password': '12456789',
            },
        )
        self.assertTrue(response)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTemplateUsed((response, 'redline/index.html'))
