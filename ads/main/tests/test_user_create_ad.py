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
        new_user_registration(self)
        login = self.selenium.find_element(By.NAME, 'login')
        login.click()
        username = self.selenium.find_element(By.NAME, 'username')
        username.send_keys('Анжелика')
        password = self.selenium.find_element(By.NAME, 'password')
        password.send_keys('SavoskoSasha21')
        login_button = self.selenium.find_element(By.TAG_NAME, 'button')
        login_button.click()
        new_ad = self.selenium.find_element(By.NAME, 'profile_new_ad')
        new_ad.click()
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('House')
        content = self.selenium.find_element(By.NAME, 'content')
        content.send_keys('House content')
        price = self.selenium.find_element(By.NAME, 'price')
        price.send_keys(120000)
        add_button = self.selenium.find_element(By.TAG_NAME, 'button')
        add_button.click()
        self.selenium.get(self.live_server_url + '')
        assert 'House' in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()


