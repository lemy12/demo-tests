from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class DemoSelectDropdownPage:
    URL = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'

    # Select list variables
    SELECT_LIST_DROPDOWN = (By.ID, 'select-demo')
    SELECT_LIST_RESULT = (By.CLASS_NAME, 'selected-value')

    TEMP = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/select/option[3]')

    # Multi select list variables
    MSELECT_LIST_MAIN = (By.ID, 'multi-select')
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

    def check_multi_select_list(self, city, choice):
        dropdown = self.browser.find_element(*self.MSELECT_LIST_MAIN)
        dropdown_options = dropdown.find_elements_by_tag_name("option")
        result_first = self.browser.find_element(*self.MSELECT_LIST_BUTTON_FIRST)
        result_all = self.browser.find_element(*self.MSELECT_LIST_BUTTON_ALL)
        result = self.browser.find_element(*self.MSELECT_LIST_RESULT)

        action_builder = ActionChains(self.browser).move_to_element(dropdown).key_down(Keys.CONTROL)
        for name in city:
            for option in dropdown_options:
                if option.text == name:
                    action_builder.move_to_element(option).click()
        action_builder.perform()

        if choice == "first":
            ActionChains(self.browser).move_to_element(result_first).click().perform()
        elif choice == "all":
            ActionChains(self.browser).move_to_element(result_all).click().perform()

        return result.text
