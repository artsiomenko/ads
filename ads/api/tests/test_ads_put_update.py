from .factories import AdFactory
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

    def test_ads_put_update(self):
        AdFactory()
        self.selenium.get(self.live_server_url + '/api/ads/3/')
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('New title')
        add_button = self.selenium.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[4]/button')
        add_button.click()
        self.selenium.get(self.live_server_url + '/api/ads/3/')
        assert 'New title' in self.selenium.page_source
