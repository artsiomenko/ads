from .options import *
from .user_registration import new_user_registration


class RegistrationUserAndNewAdd(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    def test_register_and_login(self):
        new_user_registration(self)
        login = self.selenium.find_element(By.NAME, 'login')
        login.click()
        username = self.selenium.find_element(By.NAME, 'username')
        username.send_keys('Анжелика')
        password = self.selenium.find_element(By.NAME, 'password')
        password.send_keys('SavoskoSasha21')
        login_button = self.selenium.find_element(By.TAG_NAME, 'button')
        login_button.click()
        profile = self.selenium.find_element(By.NAME, 'profile')
        profile.click()
        logout = self.selenium.find_element(By.NAME, 'logout')
        logout.click()
        assert 'Вы успешно вышли с сайта.' in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()
