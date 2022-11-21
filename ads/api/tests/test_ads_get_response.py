from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import requests
from api.tests.factories import AdFactory


class TestResponseAdsPage(StaticLiveServerTestCase):
    def test_main_page(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)


class ViewPageAds(StaticLiveServerTestCase):
    def test_response_code(self):
        AdFactory()
        page_text = str((requests.get(self.live_server_url + '/api/')).text)
        self.assertTrue('House' in page_text)
