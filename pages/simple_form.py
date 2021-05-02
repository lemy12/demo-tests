from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DemoSimpleFormPage:
    URL = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

    # Single input form variables
    SINGLE_INPUT_TEXTBOX = (By.ID, 'user-message')
    SINGLE_INPUT_SHOW = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
    SINGLE_INPUT_MESSAGE = (By.ID, 'display')

    # Two input form variables
    TWO_INPUT_TEXTBOX_A = (By.ID, 'sum1')
    TWO_INPUT_TEXTBOX_B = (By.ID, 'sum2')
    TWO_INPUT_GET = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
    TWO_INPUT_TOTAL = (By.ID, 'displayvalue')

    # Simple form (whole website) variable
    ALL_TEXTBOXES = (By.TAG_NAME, 'input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def check_single_input(self, phrase):
        """
        Send specified phrase and manually click on show button
        :param phrase: phrase used in tests
        :return: text of result message
        """
        textbox = self.browser.find_element(*self.SINGLE_INPUT_TEXTBOX)
        show = self.browser.find_element(*self.SINGLE_INPUT_SHOW)

        ActionChains(self.browser).move_to_element(textbox).double_click().perform()
        textbox.send_keys(phrase)
        ActionChains(self.browser).move_to_element(show).click().perform()

        return self.browser.find_element(*self.SINGLE_INPUT_MESSAGE).text

    def placeholder_message(self):
        return self.browser.find_elements(*self.ALL_TEXTBOXES)

    def check_two_input(self, a, b):
        """
        Send specified values and manually click on total button
        :param a: value of first textbox
        :param b: value of second textbox
        :return: text of total message
        """
        textbox_a = self.browser.find_element(*self.TWO_INPUT_TEXTBOX_A)
        textbox_b = self.browser.find_element(*self.TWO_INPUT_TEXTBOX_B)
        get = self.browser.find_element(*self.TWO_INPUT_GET)

        textbox_a.send_keys(a)
        textbox_b.send_keys(b)
        ActionChains(self.browser).click(get).perform()

        return self.browser.find_element(*self.TWO_INPUT_TOTAL).text
