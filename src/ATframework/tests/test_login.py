import pytest
from src.ATframework.utilities.BaseTestClass import BaseTestClass
from src.ATframework.pages.LoginPage import LoginPage


class TestLogin(BaseTestClass):

    @pytest.mark.auto
    def test_cos(self):
        login_page = LoginPage(self.driver)
        login_page.go()
        login_page.email_input("email@com")
        # login_page.URL = 'google.com'
        
    