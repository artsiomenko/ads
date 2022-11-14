from .model_factories import AdFactory
from .options import *
from .user_registration import new_user_registration


class RegistrationUserAndNewAdd(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    def test_for_browser(self):
        AdFactory()
        self.selenium.get(self.live_server_url + '')

        # test_search_add
        search = self.selenium.find_element(By.NAME, 'keyword')
        search.send_keys('House')
        add_button = self.selenium.find_element(By.TAG_NAME, 'button')
        add_button.click()
        assert 'House' in self.selenium.page_source

        # test_search_add_negative
        self.selenium.get(self.live_server_url + '')
        search = self.selenium.find_element(By.NAME, 'keyword')
        search.send_keys('Car')
        add_button = self.selenium.find_element(By.TAG_NAME, 'button')
        add_button.click()
        assert 'House' not in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()


