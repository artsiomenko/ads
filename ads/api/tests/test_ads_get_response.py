from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import requests
from api.tests.factories import AdFactory


class TestResponseAdsPage(StaticLiveServerTestCase):
    def test_response_ads_api(self):
        response = self.client.get('/api/ads/')
        self.assertEqual(response.status_code, 200)


class ViewPageAds(StaticLiveServerTestCase):
    def test_response_ads_on_page(self):
        AdFactory()
        page_text = str((requests.get(self.live_server_url + '/api/ads/')).text)
        self.assertTrue('House' in page_text)


class ViewPageRubric(StaticLiveServerTestCase):
    def test_response_rubric_api(self):
        AdFactory()
        page_text = str((requests.get(self.live_server_url + '/api/ads/rubric/')).text)
        self.assertTrue('Real estate' in page_text)
