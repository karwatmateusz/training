from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageClass:

    _URL = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        # add wait for page loading
        self.driver.get(self._URL)

    """TO DO: create class with support for checking elements(+wait), check BaseElementClass"""

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((locator[0], locator[1]))
        )
