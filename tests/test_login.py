from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import USERNAME, PASSWORD
from pages.login_page import LoginPage


def login(driver):

    wait = WebDriverWait(driver,20)

    wait.until(
        EC.visibility_of_element_located(LoginPage.username)
    ).send_keys(USERNAME)

    wait.until(
        EC.visibility_of_element_located(LoginPage.password)
    ).send_keys(PASSWORD)

    wait.until(
        EC.element_to_be_clickable(LoginPage.login_button)
    ).click()

    print("Login berhasil")

    wait.until(
        EC.visibility_of_element_located(("class name","toggle-sidebar"))
    )