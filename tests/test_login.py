# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import math

from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


# @pytest.mark.
# @pytest.mark.
class TestLogin:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, urls_to_test):
        self.link = urls_to_test["signIn"]

    def test_not_filled(self, browser_set, urls_to_test):
        page = LoginPage(browser_set, self.link)
        page.open()
        page.click_submit_button()
        page.popup_should_present()
        time.sleep(5)

    def test_all_empty(self, browser_set, urls_to_test):
        page = LoginPage(browser_set, self.link)
        page.open()
        page.fill_username("                                  ")
        page.fill_password("                                  ")
        page.click_submit_button()
        page.popup_should_present()


    def test_only_username(self, browser_set, urls_to_test):
        page = LoginPage(browser_set, self.link)
        page.open()
        page.fill_username("Admin")
        page.click_submit_button()
        page.popup_should_present()

    def test_only_password(self, browser_set, urls_to_test):
        page = LoginPage(browser_set, self.link)
        page.open()
        page.fill_password("admin123")
        page.click_submit_button()
        page.popup_should_present()


    def test_all_filled(self, browser_set, urls_to_test):
        page = LoginPage(browser_set, self.link)
        page.open()
        page.fill_username("Admin")
        page.fill_password("admin123")
        page.click_submit_button()
        page.validate_entry()











