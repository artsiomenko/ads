from .options import *


class UserSearchQuery(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)
        super(UserSearchQuery, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(UserSearchQuery, cls).tearDownClass()

    def test_query_params(self):
        AdFactory(), AdFactory2()
        # test_by_keyword
        self.selenium.get(self.live_server_url + '/api/ads/?keyword=House')
        assert 'Car' not in self.selenium.page_source and 'House' in self.selenium.page_source
