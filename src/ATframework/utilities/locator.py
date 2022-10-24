from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class Locator:
    location: str
    method: str = By.CSS_SELECTOR


# from collections import namedtuple

# Locator = namedtuple("Locator", ["by", "value"])
