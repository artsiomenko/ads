from .factories import AdFactory
from .options import *


class UserSearchQuery(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    def test_for_browser(self):
        AdFactory()
        self.selenium.get(self.live_server_url + '/api/ads/?search=House_title')
        assert "House_content" in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()


