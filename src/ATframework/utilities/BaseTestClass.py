import pytest


@pytest.mark.usefixtures("driver_setup")
class BaseTestClass:

    url = None

    # def go(self):
    #     #add wait for page loading
    #     self.driver.get(self.url)