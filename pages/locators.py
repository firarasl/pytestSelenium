from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.ID, "txtUsername")
    PASSWORD_INPUT = (By.ID, "txtPassword")
    SUBMIT_BUTTON = (By.ID, "btnLogin")
    ERROR_MESSAGE=(By.ID, "spanMessage")
    VALIDATION = (By.ID, "welcome")
