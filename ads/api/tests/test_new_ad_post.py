from .options import *


class TestNewAdPost(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    @classmethod
    def tearDown(cls):
        cls.selenium.quit()

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
        assert 'Title' in self.selenium.page_source
