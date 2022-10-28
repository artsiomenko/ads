from django.test import Client
from django.test import TestCase


class SimpleTest(TestCase):
    def test_main_page(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        client = Client()
        response = client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        client = Client()
        response = client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
