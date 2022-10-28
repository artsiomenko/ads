from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from main.tests.model_factories import AdFactory
import requests


class ViewPage(StaticLiveServerTestCase):
    def test_response_code(self):
        client = Client()
        ad = AdFactory()
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        page_text = str((requests.get(self.live_server_url + '')).text)
        self.assertTrue('House' in page_text)
