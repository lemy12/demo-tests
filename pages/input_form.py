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

    def check_fname(self, name):
        name_box = self.browser.find_element(*self.FIRST_NAME)
        name_box.send_keys("a", Keys.BACKSPACE, name)

        errors = self.browser.find_elements_by_xpath("//small[@data-bv-for='first_name']")
        return errors[0].value_of_css_property('display'), errors[1].value_of_css_property('display')

    def check_lname(self, name):
        name_box = self.browser.find_element(*self.LAST_NAME)
        name_box.send_keys("a", Keys.BACKSPACE, name)

        errors = self.browser.find_elements_by_xpath("//small[@data-bv-for='last_name']")
        return errors[0].value_of_css_property('display'), errors[1].value_of_css_property('display')

    def check_email(self, email):
        email_box = self.browser.find_element(*self.EMAIL)
        email_box.send_keys("a", Keys.BACKSPACE, email)

        errors = self.browser.find_elements_by_xpath("//small[@data-bv-for='email']")
        return errors[0].value_of_css_property('display'), errors[1].value_of_css_property('display')