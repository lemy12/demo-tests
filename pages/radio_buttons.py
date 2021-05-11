from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DemoRadioButtonsPage:
    URL = 'https://www.seleniumeasy.com/test/basic-radiobutton-demo.html'

    # Radio button variables
    RADIO_BUTTON_AB = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/label')
    RADIO_BUTTON_GETVALUE = (By.ID, 'buttoncheck')
    RADIO_BUTTON_RESULT = (By.CLASS_NAME, 'radiobutton')

    # Group radio buttons variables
    GROUP_RADIO_BUTTONS_SEX = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label')
    GROUP_RADIO_BUTTONS_AGE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label')
    GROUP_RADIO_BUTTONS_GETVALUES = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/button')
    GROUP_RADIO_BUTTONS_RESULT = (By.CLASS_NAME, 'groupradiobutton')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_radio_button(self, sex):
        """
        Click on specified radio and then click on "get value" button
        :param sex: Chosen sex (string)
        :return: Text of result (string)
        """
        radios = self.browser.find_elements(*self.RADIO_BUTTON_AB)
        button = self.browser.find_element(*self.RADIO_BUTTON_GETVALUE)
        result = self.browser.find_element(*self.RADIO_BUTTON_RESULT)

        for each in radios:
            if each.text.lower() == sex:
                ActionChains(self.browser).move_to_element(each).click().perform()

        ActionChains(self.browser).move_to_element(button).click().perform()

        return result.text

    def check_group_radio_buttons(self, sex, age):
        """
        Click on specified radios and then click "get values" button
        :param sex: Chosen sex (string)
        :param age: Chosen age (string)
        :return: Text of result (string)
        """
        radios_sex = self.browser.find_elements(*self.GROUP_RADIO_BUTTONS_SEX)
        radios_age = self.browser.find_elements(*self.GROUP_RADIO_BUTTONS_AGE)
        button = self.browser.find_element(*self.GROUP_RADIO_BUTTONS_GETVALUES)
        result = self.browser.find_element(*self.GROUP_RADIO_BUTTONS_RESULT)

        for each in radios_sex:
            if each.text.lower() == sex:
                ActionChains(self.browser).move_to_element(each).click().perform()

        for each in radios_age:
            if each.text.lower() == age:
                ActionChains(self.browser).move_to_element(each).click().perform()

        ActionChains(self.browser).move_to_element(button).click().perform()

        return result.text
