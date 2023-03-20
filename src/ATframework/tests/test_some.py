from pages.SomePage import SomePage
from utilities.logger import Logger
import logging
from utilities.BaseTestClass import BaseTestClass
import pytest
from utilities.logger import Logger as ca

class TestSome(BaseTestClass):

    log = ca(logging.DEBUG)

    @pytest.mark.test
    # @pytest.mark.auto
    def test_trzy(self):
        self.log.info("info message")
        page = SomePage(self.driver)
        page.go()
        second_page = page.switch_page()
        second_page.doSomething()
