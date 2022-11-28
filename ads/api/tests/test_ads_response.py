from .options import *


class TestApiAdsPOST(TestCase):
    def test_api_ads_POST(self):
        client = APIClient()
        request = client.post('/api/ads/',
                              {'title': 'new idea', 'context': 'new idea context', 'price': 15000},
                              format='json')
        assert request.status_code == 201


class TestApiAdsPUT(StaticLiveServerTestCase):
    def test_api_ads_PUT(self):
        client = APIClient()
        AdFactory()
        request = client.put('/api/ads/10/', {'title': 'new_idea'})
        assert request.status_code == 200
        page_text = str((requests.get(self.live_server_url + '/api/ads/10/')).text)
        self.assertTrue('new_idea' in page_text)


class TestApiAdsGET(StaticLiveServerTestCase):
    def test_api_ads_list_and_detail_GET(self):
        client = APIClient()
        AdFactory(), AdFactory2()
        request = client.get('/api/ads/')
        assert request.status_code == 200
        page_text = str((requests.get(self.live_server_url + '/api/ads/')).text)
        self.assertTrue(('House_title' and 'Car_title') in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/ads/20/')).text)
        self.assertTrue('Car_title' in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/ads/10/')).text)
        self.assertTrue('House_title' in page_text)


class TestResponseAdsPage(StaticLiveServerTestCase):
    def test_response_ads_api(self):
        response = self.client.get('/api/ads/')
        self.assertEqual(response.status_code, 200)


class ViewPageRubric(StaticLiveServerTestCase):
    def test_response_rubric_api(self):
        AdFactory()
        page_text = str((requests.get(self.live_server_url + '/api/ads/rubrics/')).text)
        self.assertTrue('Real estate' in page_text)
