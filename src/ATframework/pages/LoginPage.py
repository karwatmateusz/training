from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement


class LoginPage(BasePageClass):

    _URL = "http://automationpractice.com/index.php?controller=my-account"
    email_locator = (By.CSS_SELECTOR, '#email')
    password_locator = (By.CSS_SELECTOR, '#passwd')
    login_locator = (By.CSS_SELECTOR, '#SubmitLogin')

    def __init__(self, driver):
        self.driver = driver
    
    def email_input(self, email):
        # email_field = self.verify_element(self.email_locator)
        # email_field.send_keys(email)
        email_field = BaseElement(self.driver, self.email_locator)
        email_field.insert_text(email)

    def password_input(self, password):
        # password_field = self.verify_element(self.password_locator)
        # password_field.send_keys(password)
        password_field = BaseElement(self.driver, self.password_locator)
        password_field.insert_text(password)
    
    def login_button_click(self):
        # login_button = self.verify_element(self.login_locator)
        # login_button.click()
        login_button = BaseElement(self.driver, self.login_locator)
        login_button.click_field()

    def get_url(self):
        return self.driver.current_url