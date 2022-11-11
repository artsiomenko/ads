from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from django.test import TestCase
import requests

from main.tests.model_factories import AdFactory


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


class ViewPage(StaticLiveServerTestCase):
    def test_response_code(self):
        client = Client()
        ad = AdFactory()
        response = self.client.get('')
        page_text = str((requests.get(self.live_server_url + '')).text)
        self.assertTrue('House' in page_text)
