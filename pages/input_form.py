from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class DemoInputFormPage:
    URL = 'https://www.seleniumeasy.com/test/input-form-demo.html'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_errors(self, text, input_type):
        textbox = self.browser.find_element_by_name(input_type)
        textbox.send_keys("a", Keys.BACKSPACE, text)

        errors = self.browser.find_elements_by_xpath("//small[@data-bv-for='" + input_type + "']")
        return {errors[i].get_attribute("data-bv-validator"): errors[i].value_of_css_property('display')
                for i in range(0, len(errors))}

    def check_error_state(self, state):
        states_list = Select(self.browser.find_element_by_name("state"))
        states_list.select_by_visible_text(state)

        return self.browser.find_element_by_xpath("//small[@data-bv-for='state']").value_of_css_property('display')

    def check_radios(self, radio):
        radio_element = self.browser.find_element_by_xpath("//input[@value='" + radio + "']")
        ActionChains(self.browser).move_to_element(radio_element).click().perform()

    def check_send_button(self):
        button = self.browser.find_element_by_class_name("btn btn-default")
        return button.get_attribute("disabled")
