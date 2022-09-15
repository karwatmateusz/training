import pytest
import selenium
from utilities.BaseTestClass import BaseTestClass


class TestLogin(BaseTestClass):

    def test_login(self):
        print("Test started")
        print(self.driver)