from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
import requests
from api.tests.factories import AdFactory


class TestResponseAdsPage(StaticLiveServerTestCase):
    def test_main_page(self):
        client = Client()
        response = self.client.get('/api/ads/')
        self.assertEqual(response.status_code, 200)


class ViewPageAds(StaticLiveServerTestCase):
    def test_response_code(self):
        client = Client()
        ad = AdFactory()
        response = self.client.get('/api/ads/')
        page_text = str((requests.get(self.live_server_url + '/api/ads/')).text)
        self.assertTrue('House' in page_text)
