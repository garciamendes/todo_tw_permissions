# Django
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client


class CoreTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client
        self.maxDiff = None

    def create_user(self):
        User = get_user_model()

        user = User.objects.create(
            username='teste_case',
            email='teste_case@example.com',
            first_name='teste_case',
            last_name='teste_case')

        user.set_password('dev12345')
        user.save()

        return user

    def create_and_login_user_teste(self):
        self.user = self.create_user()

        response = self.client.post(
            'api/auth/login/',
            {'email': self.user.email, 'password': 'dev12345'})

        self.data = response.data
        return
