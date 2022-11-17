from .factories import AdFactory, AdFactory2
from .options import *


class UserSearchQuery(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        cls.selenium = WebDriver(chrome_options=options)

    @classmethod
    def tearDown(cls):
        cls.selenium.quit()

    def test_query_params(self):
        AdFactory(), AdFactory2()
        # test_by_rubric
        self.selenium.get(self.live_server_url + '/api/?rubric=1')
        assert 'House' in self.selenium.page_source and 'Car' not in self.selenium.page_source
        self.selenium.get(self.live_server_url + '/api/?rubric=2')
        assert 'Car' in self.selenium.page_source and 'House' not in self.selenium.page_source
        # test_by_author
        self.selenium.get(self.live_server_url + '/api/?author=1')
        assert 'House' in self.selenium.page_source and 'Car' not in self.selenium.page_source
        self.selenium.get(self.live_server_url + '/api/?author=2')
        assert 'Car' in self.selenium.page_source and 'House' not in self.selenium.page_source
        # test_by_author_and_rubric
        self.selenium.get(self.live_server_url + '/api/?author=2&rubric=2')
        assert 'Car' in self.selenium.page_source and 'House' not in self.selenium.page_source
        self.selenium.get(self.live_server_url + '/api/?author=1&rubric=2')
        assert 'Car' not in self.selenium.page_source and 'House' not in self.selenium.page_source
        # test_by_keyword
        self.selenium.get(self.live_server_url + '/api/?keyword=House')
        assert 'Car' not in self.selenium.page_source and 'House' in self.selenium.page_source



