from .options import *
from .user_registration import new_user_registration


class RegistrationUser(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    def test_register(self):
        new_user_registration(self)
        assert 'Регистрация пользователя завершена.' in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()
