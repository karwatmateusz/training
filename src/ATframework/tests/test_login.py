import pytest
from utilities.BaseTestClass import BaseTestClass
from pages.LoginPage import LoginPage


class TestLogin(BaseTestClass):

    @pytest.mark.auto
    def test_cos(self):
        login_page = LoginPage(self)
        login_page.email_input(email="email@gmail.com")