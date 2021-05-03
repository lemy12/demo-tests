from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DemoCheckboxPage:
    URL = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'

    # Single checkbox variables
    SINGLE_CHECKBOX_A = (By.ID, 'isAgeSelected')
    SINGLE_CHECKBOX_RESULT = (By.ID, 'txtAge')

    # Multiple checkbox variables
    MULTIPLE_CHECKBOX_ABCD = (By.CLASS_NAME, 'cb1-element')
    MULTIPLE_CHECKBOX_CHECKALL = (By.ID, 'check1')
    MULTIPLE_CHECKBOX_VALUE = (By.ID, 'isChkd')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_single_checkbox(self):
        """
        Click on specified checkbox
        :return: value of display css property of show message
        """
        checkbox = self.browser.find_element(*self.SINGLE_CHECKBOX_A)
        show = self.browser.find_element(*self.SINGLE_CHECKBOX_RESULT)

        ActionChains(self.browser).move_to_element(checkbox).click().perform()

        return show.value_of_css_property('display')

    def check_multiple_checkall_button(self):
        """
        Click on specified button
        :return: Value of hidden element and value of check/uncheck all button
        """
        checkall = self.browser.find_element(*self.MULTIPLE_CHECKBOX_CHECKALL)
        check_hidden = self.browser.find_element(*self.MULTIPLE_CHECKBOX_VALUE)

        ActionChains(self.browser).move_to_element(checkall).click().perform()

        return check_hidden.get_attribute("value"), checkall.get_attribute("value")

    def check_multiple_checkall_manual(self):
        """
        Click on specified checkboxes
        :return: Value of hidden element and value of check/uncheck all button
        """
        checkall = self.browser.find_element(*self.MULTIPLE_CHECKBOX_CHECKALL)
        check_hidden = self.browser.find_element(*self.MULTIPLE_CHECKBOX_VALUE)
        checkboxes = self.browser.find_elements(*self.MULTIPLE_CHECKBOX_ABCD)

        for each in checkboxes:
            ActionChains(self.browser).move_to_element(each).click().perform()

        return check_hidden.get_attribute("value"), checkall.get_attribute("value")