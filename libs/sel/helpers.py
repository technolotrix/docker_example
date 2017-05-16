import os
import re

import selenium

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.switch_to import SwitchTo

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException as Stale

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from libs.sel.basedriver import WAIT

def _re(query, val):
    return re.search(query, val, re.I)


class CustomActions():

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        try:
            element = self.driver.find_element(*locator)
        except (NoSuchElementException, ElementNotVisibleException, Stale) as e:
            return False
        return element

    def find_and_click(self, locator):
        element = self.find(locator)

        if element:
            element.click()
        return element

    def send_keys(self, locator, keys):
        locator = self.find(locator)
        locator.send_keys(keys)

    def fill_out_form(self, locator, text):
        element = self.find(locator)

        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        element = self.find(locator)

        if element:
            try:
                text = element.text
            except Exception as e:
                print(str(e))
                return ''
            return text
        return ''
