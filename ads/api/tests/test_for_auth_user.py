from .options import *


class TestApiAdsGETUserAuth(StaticLiveServerTestCase):
    def test_api_ads_list_and_detail_auth_user_GET(self):
        password = 'password'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        client = Client()
        client.login(username=my_admin.username, password=password)
        AdFactory(), AdFactory2()
        request = client.get('/api/v1/ads/')
        assert request.status_code == 200
        page_text = str((requests.get(self.live_server_url + '/api/v1/ads/')).text)
        self.assertTrue(('House_title' and 'Car_title') in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/v1/ads/20/')).text)
        self.assertTrue('Car_title' in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/v1/ads/10/')).text)
        self.assertTrue('House_title' in page_text)

    def test_api_ads_list_and_detail_not_auth_user_GET(self):
        client = Client()
        AdFactory(), AdFactory2()
        request = client.get('/api/v1/ads/')
        assert request.status_code == 200
        page_text = str((requests.get(self.live_server_url + '/api/v1/ads/')).text)
        self.assertTrue(('House_title' and 'Car_title') in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/v1/ads/20/')).text)
        self.assertTrue('Car_title' in page_text)
        page_text = str((requests.get(self.live_server_url + '/api/v1/ads/10/')).text)
        self.assertTrue('House_title' in page_text)


# class TestApiAdsAuthUserPUT(StaticLiveServerTestCase):
#     def test_api_ads_auth_user_PUT(self):
#         AdFactory()
#         password = 'password'
#         my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
#         # client = Client()
#         # client.login(username=my_admin.username, password=password)
#         self.client.login(username=my_admin.username, password=password)
#         self.client.put('/api/v1/ads/10/', {'title': 'new_idea'})
#         # assert request.status_code == 200
#         page_text = str((requests.get(self.live_server_url + '/api/v1/ads/10/')).text)
#         self.assertTrue('new_idea' in page_text)
