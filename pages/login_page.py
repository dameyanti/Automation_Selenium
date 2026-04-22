from selenium.webdriver.common.by import By

class LoginPage:

    username = (By.ID, "username")

    password = (By.ID, "password")

    login_button = (By.ID, "kc-login")