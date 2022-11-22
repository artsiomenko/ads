import time

from .options import *


class TestNewAdPost(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)
        super(TestNewAdPost, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestNewAdPost, cls).tearDownClass()

    def test_new_ad_post(self):
        self.selenium.get(self.live_server_url + '/api/ads/')
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('title')
        content = self.selenium.find_element(By.NAME, 'content')
        content.send_keys('content')
        price = self.selenium.find_element(By.NAME, 'price')
        price.send_keys(120000)
        add_button = self.selenium.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
        add_button.click()
        self.selenium.get(self.live_server_url + '/api/ads/')
        assert 'Title' in self.selenium.page_source

    def test_ads_put_update(self):
        AdFactory()
        self.selenium.get(self.live_server_url + '/api/ads/1/')
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys(' New title')
        put = self.selenium.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[4]/button')
        put.click()
        self.selenium.get(self.live_server_url + '/api/ads/')
        assert 'New title' in self.selenium.page_source
