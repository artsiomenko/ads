from .options import *


class TestAdUpdate(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    @classmethod
    def tearDown(cls):
        cls.selenium.quit()

    def test_ad_update(self):
        self.selenium.get(self.live_server_url + '/ads/')
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('title')
        content = self.selenium.find_element(By.NAME, 'content')
        content.send_keys('content')
        price = self.selenium.find_element(By.NAME, 'price')
        price.send_keys(120000)
        add_button = self.selenium.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
        add_button.click()
        self.selenium.get(self.live_server_url + '/ads/1/')
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('New title')
        add_button = self.selenium.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[4]/button')
        add_button.click()
        self.selenium.get(self.live_server_url + '/ads/1/')
        assert 'New title' in self.selenium.page_source
