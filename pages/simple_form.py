from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class DemoSimpleFormPage:
    URL = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

    SINGLE_INPUT_TEXTBOX = (By.ID, 'user-message')
    SINGLE_INPUT_SHOW = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
    SINGLE_INPUT_MESSAGE = (By.ID, 'display')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_single_input(self, phrase):
        textbox = self.browser.find_element(*self.SINGLE_INPUT_TEXTBOX)
        textbox.send_keys(phrase)
        show = self.browser.find_element(*self.SINGLE_INPUT_SHOW)
        ActionChains(self.browser).move_to_element(show).click().perform()
        return self.browser.find_element(*self.SINGLE_INPUT_MESSAGE).text
