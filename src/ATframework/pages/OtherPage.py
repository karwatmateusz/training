from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement
from utilities.locator import Locator


class OtherPage(BasePageClass):

    locator = Locator("#search_form_input")

    def doSomething(self):
        print("wyswietlam cos")
        field = BaseElement(self.driver, self.locator)
        field.insert_text("something new")
        print("zmieniam tekst")
