from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DemoRadioButtonsPage:
    URL = 'https://www.seleniumeasy.com/test/basic-radiobutton-demo.html'

    # Radio button variables
    RADIO_BUTTON_AB = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/label')
    RADIO_BUTTON_GETVALUE = (By.ID, 'buttoncheck')
    RADIO_BUTTON_RESULT = (By.CLASS_NAME, 'radiobutton')

    # Group radio buttons variables
    GROUP_RADIO_BUTTONS_SEX = (By.CLASS_NAME, 'gender')
    GROUP_RADIO_BUTTONS_AGE = (By.CLASS_NAME, 'ageGroup')
    GROUP_RADIO_BUTTONS_GETVALUES = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/button')
    GROUP_RADIO_BUTTONS_RESULT = (By.CLASS_NAME, 'groupradiobutton')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_radio_button(self):
        """
        Click on every radio button
        :return: List of radio button with variables corresponding to their text and given result
        """
        radios = self.browser.find_elements(*self.RADIO_BUTTON_AB)
        button = self.browser.find_element(*self.RADIO_BUTTON_GETVALUE)
        result = self.browser.find_element(*self.RADIO_BUTTON_RESULT)

        radio_result_list = []

        for each in radios:
            ActionChains(self.browser).move_to_element(each).click().perform()
            ActionChains(self.browser).move_to_element(button).click().perform()
            radio_result_list.append([each.text, result.text])

        return radio_result_list
