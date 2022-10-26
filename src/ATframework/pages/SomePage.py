from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement
from utilities.locator import Locator
from pages.OtherPage import OtherPage


class SomePage(BasePageClass):

    _URL = "https://duckduckgo.com/"

    locator = Locator("#searchbox_input")
    locator_search = Locator(
        "#searchbox_homepage > div > div > button.searchbox_searchButton__F5Bwq.iconButton_button__6x_9C"
    )

    def switch_page(self) -> OtherPage:
        button = BaseElement(self.driver, self.locator)
        button.insert_text("test")
        print("wpisalem tekst")
        search = BaseElement(self.driver, self.locator_search)
        search.click_field()
        print("kliknalem cos")
        return OtherPage(self.driver)
