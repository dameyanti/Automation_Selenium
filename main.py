from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from config.config import BASE_URL, GECKO_PATH, FIREFOX_PATH

from tests.test_login import login
from tests.test_dashboard import open_tracking_system
from tests.test_tracking import test_tracking_pages


options = Options()
options.binary_location = FIREFOX_PATH

service = Service(GECKO_PATH)

driver = webdriver.Firefox(service=service, options=options)

driver.maximize_window()

driver.get(BASE_URL)

login(driver)

open_tracking_system(driver)

test_tracking_pages(driver)

input("Press Enter to close browser...")

driver.quit()