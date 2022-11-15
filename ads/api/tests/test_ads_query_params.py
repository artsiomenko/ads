from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
import requests
from api.tests.factories import AdFactory, AdFactory2


class ViewPageAdsByRubric(StaticLiveServerTestCase):
    def test_query_params(self):
        client = Client()
        ad, ad2 = AdFactory(), AdFactory2()
        page_text = str((requests.get(self.live_server_url + '/api/ads/?rubric_id=1')).text)
        self.assertTrue('House' in page_text and 'Car' not in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/ads/?rubric_id=2')).text)
        self.assertTrue('Car' in page_text and 'House' not in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/ads/?author_id=1')).text)
        self.assertTrue('House' in page_text and 'Car' not in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/ads/?author_id=2')).text)
        self.assertTrue('Car' in page_text and 'House' not in page_text)


