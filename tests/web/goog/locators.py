from selenium.webdriver.common.by import By


class GoogleSearchLocators(object):

        SEARCH_BAR = (By.CSS_SELECTOR, '#lst-ib')
        SEARCH_BUTTON = (
                By.CSS_SELECTOR, '#_fZl > span > svg'
                )

        FEELING_LUCKY_BUTTON = (
                By.ID,
                '#gbqfbb')

        SEARCH_RESULTS = (
            By.CSS_SELECTOR, # format w/ n for n results
            '#rso > div:nth-child({}) > div > div:nth-child(1) > div > div > h3 > a'
            )