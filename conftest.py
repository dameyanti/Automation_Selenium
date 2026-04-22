import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from config.config import BASE_URL, GECKO_PATH, FIREFOX_PATH


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = FIREFOX_PATH

    service = Service(GECKO_PATH)

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()