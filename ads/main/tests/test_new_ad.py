# from .options import *
#
#
# class RegistrationUserAndNewAdd(StaticLiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         options = Options()
#         options.add_argument('--headless')
#         cls.selenium = WebDriver(chrome_options=options)
#
#     def test_adding_new_ad(self):
#         self.selenium.get(self.live_server_url + '')
#         register = self.selenium.find_element(By.NAME, 'register')
#         register.click()
#         username = self.selenium.find_element(By.NAME, 'username')
#         username.send_keys('Анжелика')
#         email = self.selenium.find_element(By.NAME, 'email')
#         email.send_keys('aya@anadeainc.com')
#         password1 = self.selenium.find_element(By.NAME, 'password1')
#         password1.send_keys('SavoskoSasha21')
#         password2 = self.selenium.find_element(By.NAME, 'password2')
#         password2.send_keys('SavoskoSasha21')
#         first_name = self.selenium.find_element(By.NAME, 'first_name')
#         first_name.send_keys('Анжелика')
#         last_name = self.selenium.find_element(By.NAME, 'last_name')
#         last_name.send_keys('Артеменко')
#         registration_button = self.selenium.find_element(By.TAG_NAME, 'button')
#         registration_button.click()
#         login = self.selenium.find_element(By.NAME, 'login')
#         login.click()
#         username = self.selenium.find_element(By.NAME, 'username')
#         username.send_keys('Анжелика')
#         password = self.selenium.find_element(By.NAME, 'password')
#         password.send_keys('SavoskoSasha21')
#         login_button = self.selenium.find_element(By.TAG_NAME, 'button')
#         login_button.click()
#
#         #  test_adding_new_add(self):
#         new_ad = self.selenium.find_element(By.NAME, 'profile_new_ad')
#         new_ad.click()
#         title = self.selenium.find_element(By.NAME, 'title')
#         title.send_keys('House')
#         content = self.selenium.find_element(By.NAME, 'content')
#         content.send_keys('House content')
#         price = self.selenium.find_element(By.NAME, 'price')
#         price.send_keys(120000)
#         time.sleep(1)
#         add_button = self.selenium.find_element(By.TAG_NAME, 'button')
#         add_button.click()
#         self.selenium.get(self.live_server_url + '')
#         time.sleep(1)
#         assert 'House' in self.selenium.page_source
#
#     def tearDown(self):
#         self.selenium.quit()
#
#
