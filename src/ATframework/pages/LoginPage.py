from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseInputField import BaseInputField


class LoginPage(BasePageClass):

    _URL = "https://demo.opencart.com/index.php?route=account/login"
    email_locator = (By.CSS_SELECTOR, '#input-email')
    password_locator = (By.CSS_SELECTOR, '#input-password')
    login_locator = (By.CSS_SELECTOR, '#form-login > button')

    def __init__(self, driver):
        self.driver = driver
    
    def email_input(self, email):
        # email_field = self.verify_element(self.email_locator)
        # email_field.send_keys(email)
        email_field = BaseInputField(self.driver, self.email_locator)
        email_field.insert_text(email)

    def password_input(self, password):
        password_field = self.verify_element(self.password_locator)
        password_field.send_keys(password)
    
    def login_button_click(self):
        login_button = self.verify_element(self.login_locator)
        login_button.click()
