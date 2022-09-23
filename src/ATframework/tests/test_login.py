import pytest
from src.ATframework.utilities.BaseTestClass import BaseTestClass
from src.ATframework.pages.LoginPage import LoginPage


class TestLogin(BaseTestClass):

    @pytest.mark.auto
    def test_cos(self):
        login_page = LoginPage(self.driver)
        login_page.go()
        login_page.email_input("jktest1233@gmail.com")
        login_page.password_input("12345")
        login_page.login_button_click()
        assert login_page.element_is_visible, 'Log in failed'
        # assert 'language' in login_page.get_url()
