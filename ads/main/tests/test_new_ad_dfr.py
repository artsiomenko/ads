from .model_factories import UserFactory, RubricFactory
from .options import *
from selenium.webdriver.support.select import Select


class RegistrationUserAndNewAdd(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    def test_adding_new_ad(self):
        self.selenium.get(self.live_server_url + '/api/ads/')

        #  test_adding_new_add(self):
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('House')
        content = self.selenium.find_element(By.NAME, 'content')
        content.send_keys('House content')
        price = self.selenium.find_element(By.NAME, 'price')
        price.send_keys(120000)
        time.sleep(1)
        add_button = self.selenium.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[6]/button')
        add_button.click()
        self.selenium.get(self.live_server_url + '/api/ads/')
        time.sleep(1)
        assert 'House' in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()


