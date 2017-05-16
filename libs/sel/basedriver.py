from config import APP_SETTINGS
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

VALID_BROWSERS = ["chrome", "firefox", "phantomjs"]
WAIT = 3


class BaseDriver():

    def __init__(self):

        self.browser = APP_SETTINGS.BROWSER
        self.run_local = APP_SETTINGS.LOCAL_SELENIUM

        if self.browser not in VALID_BROWSERS:
            raise Exception("Invalid browser!  Allowed types are {0}".format(VALID_BROWSERS))

        self.make_driver()

    def make_local_driver(self):
        if self.browser == "firefox":
            self.driver = webdriver.Firefox()

        if self.browser == "chrome":
            self.driver = webdriver.Chrome()

        if self.browser == "phantomjs":
            self.driver = webdriver.PhantomJS()

    def make_remote_driver(self):

        if self.browser == "firefox":
            self.driver = webdriver.Remote(
                command_executor=APP_SETTINGS.COMMAND_EXECUTOR,
                desired_capabilities=DesiredCapabilities.FIREFOX)

        if self.browser == "chrome":
            self.driver = webdriver.Remote(
                '/usr/bin/chromedriver',
                command_executor=APP_SETTINGS.COMMAND_EXECUTOR)

        if self.browser == "phantomjs":
            self.driver = webdriver.Remote(
                command_executor=APP_SETTINGS.COMMAND_EXECUTOR,
                desired_capabilities=DesiredCapabilities.PHANTOMJS)

    def set_window_size(self):
        self.driver.implicitly_wait(WAIT)
        #self.driver.set_window_size(1200,1080)

    def make_driver(self):
        if self.run_local:
            self.make_local_driver()
        else:
            self.make_remote_driver()

        self.set_window_size()
