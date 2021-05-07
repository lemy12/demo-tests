from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class DemoSelectDropdownPage:
    URL = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'

    # Select list variables
    SELECT_LIST_DROPDOWN = (By.ID, 'select-demo')
    SELECT_LIST_DROPDOWN_OPTIONS = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/select/option')
    SELECT_LIST_RESULT = (By.CLASS_NAME, 'selected-value')

    TEMP = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/select/option[3]')

    # Multi select list variables
    MSELECT_LIST_OPTIONS = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/select/option')
    MSELECT_LIST_BUTTON_FIRST = (By.ID, 'printMe')
    MSELECT_LIST_BUTTON_ALL = (By.ID, 'printAll')
    MSELECT_LIST_RESULT = (By.CLASS_NAME, 'getall-selected')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_select_list(self, day):
        dropdown = Select(self.browser.find_element(*self.SELECT_LIST_DROPDOWN))
        result = self.browser.find_element(*self.SELECT_LIST_RESULT)

        dropdown.select_by_value(day)

        return result.text
