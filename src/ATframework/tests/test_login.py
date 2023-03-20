import pytest
import allure
from src.ATframework.utilities.BaseTestClass import BaseTestClass
from src.ATframework.pages.LoginPage import LoginPage
from utilities.logger import Logger as ca
import logging


class TestLogin(BaseTestClass):

    URL = "https://google.com/"
    log = ca(logging.DEBUG)
    @pytest.mark.auto
    # @allure.flaky
    @allure.title("This test has a custom title")
    def test_cos(self, driver_setup):
        self.log.debug("debug message")
        # print("elo")
        # self.log.info("info message")
        # print("some action")
        # x = 1
        # self.log.error(f"error happened {x}")
        # # driver_setup.get(self.URL)
        # self.log.info("moved to URL")
        # assert True
        # return
        login_page = LoginPage(self.driver)
        login_page.go()
        login_page.email_input("tomsmith")
        login_page.password_input("SuperSecretPassword!")
        login_page.login_button_click()
        # assert login_page.element_is_visible, "Log in failed"
        assert 'secure' in login_page.get_url()

    # @pytest.mark.auto
    def test_dwa(self):
        self.log.info("second test")
        assert True
