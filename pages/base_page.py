from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_element(self, how, what):

        assert self.is_element_present(how, what, timeout=3),\
            f'Cannot get element "{str(how)}.{str(what)}"'
        return self.browser.find_element(how, what)

    def get_element_if_clickable(self, how, what):
        assert self.is_element_present(how, what, timeout=3),\
            f'Cannot get element "{str(how)}.{str(what)}"'
        assert self.is_element_clickable(how, what, timeout=3),\
            f'Element "{str(how)}.{str(what)}" is not clickable'
        return self.browser.find_element(how, what)

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def get_all_elements(self, how, what):
        assert self.are_elements_present(how, what),\
            f'Cannot get elementS "{str(how)}.{str(what)}"'
        return self.browser.find_elements(how, what)

    def are_elements_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_clickable(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def is_appeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    @staticmethod
    def is_same_link(actual, expected):
        assert actual == expected, "Wrong redirection link"


