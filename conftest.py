import codecs
import json

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def configuration():
    with codecs.open('config.json', 'r', encoding='utf8') as json_file:
        data = json.load(json_file)

    for i in data["urlsToTest"]:
        value = data["urlsToTest"][i]
        data["urlsToTest"][i] = value.replace("{clientAppUrl}", data["clientAppUrl"])

    return data

@pytest.fixture(scope="class")
def urls_to_test(configuration):
    return configuration["urlsToTest"]

@pytest.fixture(scope="function")
def browser_set(configuration):
    options = Options()
    options.add_argument('--ignore-broker-pipe-errors')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # browser = webdriver.Chrome(options=options)

    # browser = webdriver.Chrome(ChromeDriverManager().install())

    browser = webdriver.Chrome(r"C:/Users/firar/PycharmProjects/chromedriver.exe")
    browser.maximize_window()
    browser.implicitly_wait(10)

    client_app_url = configuration["clientAppUrl"]

    # browser = prepare_browser(browser, client_app_url, configuration)
    browser.get(client_app_url)
    yield browser

    browser.quit()



def prepare_browser(browser, client_app_url, info_url):
    browser.get(client_app_url)

    response = requests.get(info_url, verify=False)

    storage_items = {"scope": json.loads(response.content)["scope"],
                     "accessToken": response.headers["accessToken"]}
    for i in storage_items:
        browser.execute_script(f"localStorage.setItem('{i}', '{storage_items[i]}')")

    return browser


