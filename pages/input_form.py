from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class DemoInputFormPage:
    URL = 'https://www.seleniumeasy.com/test/input-form-demo.html'

    # Input form variables
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    EMAIL = (By.NAME, "email")
    PHONE = (By.NAME, "phone")
    ADDRESS = (By.NAME, "address")
    CITY = (By.NAME, "city")
    STATE = (By.NAME, "state")
    ZIP_CODE = (By.NAME, "zip")
    WEBSITE = (By.NAME, "website")
    HOSTING_RADIOS = (By.NAME, "name")
    DESC = (By.NAME, "comment")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_errors(self, text, input_type):
        textbox = self.browser.find_element_by_name(input_type)
        textbox.send_keys("a", Keys.BACKSPACE, text)

        errors = self.browser.find_elements_by_xpath("//small[@data-bv-for='" + input_type + "']")
        return {errors[i].get_attribute("data-bv-validator"): errors[i].value_of_css_property('display')
                for i in range(0, len(errors)-1)}
