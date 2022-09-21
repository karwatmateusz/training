from utilities.BaseTestClass import BaseTestClass
from selenium.webdriver.common.by import By

class LoginPage():

    URL = "https://demo.opencart.com/index.php?route=account/login"
    email_locator = ''
    password_locator = ''
    login_locator = ''

    def __init__(self, driver):
        self.driver = driver
    
    def email_input(self, email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, self.email_locator)
        email_field.send_keys(email)

    def password_input(self, password):
        password_field = self.driver.find_element(By.CSS_SELECTOR, self.password_locator)
        password_field.send_keys(password)
    
    def login_button_click(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, self.login_locator)
        login_button.click()
