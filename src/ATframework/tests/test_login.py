import pytest
import allure
from src.ATframework.utilities.BaseTestClass import BaseTestClass
from src.ATframework.pages.LoginPage import LoginPage


class TestLogin(BaseTestClass):

    @pytest.mark.smoke
    @allure.title("This test has a custom title")
    def test_one(self):
        pass
