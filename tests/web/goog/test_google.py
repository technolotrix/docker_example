from nose.tools import assert_true

from libs.sel.basedriver import BaseDriver

from .page import GoogleSearchPage
from .data import BASEURL, QUERY

URL = BASEURL

class TestNav():

    @classmethod
    def setUpClass(self):
        self.driver = BaseDriver().driver
        self.driver.get(URL)
        self.page = GoogleSearchPage(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_search_bar_is_on_google_page(self):
        assert self.page.is_search_bar_on_page()

    def test_search_for_docker_returns_results_with_term(self):
        self.page.search_for_term(QUERY)
        assert self.page.is_query_in_search_results(QUERY)
