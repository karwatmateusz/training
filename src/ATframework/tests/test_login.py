import pytest
import allure
from src.ATframework.utilities.BaseTestClass import BaseTestClass
from src.ATframework.pages.LoginPage import LoginPage
from utilities.logger import Logger
import logging


class TestLogin(BaseTestClass):

    log = Logger(logging.DEBUG)

    @pytest.mark.auto
    # @allure.flaky
    @allure.title("This test has a custom title")
    def test_cos(self):
        self.log.debug("debug message")
        print("elo")
        self.log.info("info message")
        print("some action")
        x = 1
        self.log.error(f"error happened {x}")
        assert True
        return
        login_page = LoginPage(self.driver)
        login_page.go()
        login_page.email_input("jktest1233@gmail.com")
        login_page.password_input("12345")
        login_page.login_button_click()
        assert login_page.element_is_visible, "Log in failed"
        # assert 'language' in login_page.get_url()
