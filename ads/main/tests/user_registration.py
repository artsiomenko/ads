from selenium.webdriver.common.by import By


def new_user_registration(self):
    self.selenium.get(self.live_server_url + '')
    register = self.selenium.find_element(By.NAME, 'register')
    register.click()
    username = self.selenium.find_element(By.NAME, 'username')
    username.send_keys('Анжелика')
    email = self.selenium.find_element(By.NAME, 'email')
    email.send_keys('aya@anadeainc.com')
    password1 = self.selenium.find_element(By.NAME, 'password1')
    password1.send_keys('SavoskoSasha21')
    password2 = self.selenium.find_element(By.NAME, 'password2')
    password2.send_keys('SavoskoSasha21')
    first_name = self.selenium.find_element(By.NAME, 'first_name')
    first_name.send_keys('Анжелика')
    last_name = self.selenium.find_element(By.NAME, 'last_name')
    last_name.send_keys('Артеменко')
    registration_button = self.selenium.find_element(By.TAG_NAME, 'button')
    registration_button.click()