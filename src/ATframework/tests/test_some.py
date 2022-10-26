from pages.SomePage import SomePage
from utilities.logger import Logger
import logging
from utilities.BaseTestClass import BaseTestClass
import pytest


class TestSome(BaseTestClass):
    @pytest.mark.test
    def test_trzy(self):
        page = SomePage(self.driver)
        page.go()
        second_page = page.switch_page()
        second_page.doSomething()
