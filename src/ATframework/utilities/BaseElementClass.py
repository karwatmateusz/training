from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.locator import Locator


class BaseElement:
    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.element = self.verify_element(self.locator)

    def insert_text(self, text):
        # field = self.verify_element(self.locator)
        self.element.send_keys(text)

    def click_field(self):
        # field = self.verify_element(self.locator)
        self.element.click()

    """TO DO: create class with support for checking elements(+wait), check BasePageClass"""

    def verify_element(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((locator.method, locator.location))
        )
        # element = self.driver.find_element(locator[0], locator[1])
        # return element
