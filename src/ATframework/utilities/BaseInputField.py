from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseInputField():

    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator

    def insert_text(self, text):
        field = self.verify_element(self.locator)
        field.send_keys(text)

    def verify_element(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((locator[0], locator[1])))
        # element = self.driver.find_element(locator[0], locator[1])
        # return element