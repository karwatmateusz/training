import pytest
from utilities.logger import Logger as ca
import logging

@pytest.mark.usefixtures("driver_setup")
# @pytest.mark.usefixtures("take_screenshot")
class BaseTestClass:

    url = None

    # def go(self):
    #     #add wait for page loading
    #     self.driver.get(self.url)
