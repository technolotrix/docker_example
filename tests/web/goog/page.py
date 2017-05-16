from . import data
from .locators import GoogleSearchLocators as GSL
from libs.sel.helpers import CustomActions, _re


class GoogleSearchPage():

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)

    def is_search_bar_on_page(self):
        return self.find_search_bar()

    def is_query_in_search_results(self, query):
        return _re(query, self.get_search_results_text(1))
        #return query in self.get_search_results_text(1)

    def find_search_bar(self):
        return self.helpers.find(GSL.SEARCH_BAR)

    def search_for_term(self, query):
        self.helpers.fill_out_form(
            GSL.SEARCH_BAR, query)
        self.helpers.find_and_click(GSL.SEARCH_BUTTON)

    def get_search_results_text(self, n):
        new_locator = (
            GSL.SEARCH_RESULTS[0],
            GSL.SEARCH_RESULTS[1].format(str(n))
            )

        elem = self.helpers.get_text(new_locator)
        return elem

