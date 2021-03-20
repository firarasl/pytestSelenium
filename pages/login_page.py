from selenium.webdriver.common.by import By
from time import sleep

from .base_page import BasePage
from .locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(BasePage):

    def fill_username(self, text):
        element = self.get_element_if_clickable(*LoginLocators.USERNAME_INPUT)
        element.send_keys(text)

    def fill_password(self, text):
        element = self.get_element_if_clickable(*LoginLocators.PASSWORD_INPUT)
        element.send_keys(text)

    def click_submit_button(self):
        element = self.get_element_if_clickable(*LoginLocators.SUBMIT_BUTTON)
        element.click()

    def popup_should_present(self):
        assert self.is_appeared(*LoginLocators.ERROR_MESSAGE), "Login error popup is not present"


    def validate_entry(self):
        assert self.is_element_present(*LoginLocators.VALIDATION), "Login failed"


