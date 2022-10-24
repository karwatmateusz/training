from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

"""Fixture to install webdriver"""
@pytest.fixture(scope="class", autouse=True)
def driver_setup(request):
    print("\nSetting up browser")
    if browser_selected=='chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        print("Please select chrome as a browser")
    driver.maximize_window()
    request.cls.driver = driver
    print("\nBrowser up and running")
    yield driver
    print("\nTesting finished \nClosing browser")
    driver.quit()


"""Fixture to take screenshot after test fail
Save screenshot and attach it to allure test report"""
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def attach_screenshot_on_fail(request):
    if request.node.rep_call.failed:
        print("Test execution for {request.node.name} failed, taking a screenshot")
        driver = request.cls.driver
        file_name = f'{request.node.name}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace(
            "/", "_"
        ).replace(
            "::", "__"
        )
        take_screenshot(driver, file_name)
        print("Screenshot saved")   
        attach_screenshot_to_report(file_name)
        print("Screenshot attached to the report")
    else:
        print("Test {request.node.name} passed")

def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
    return file_name

def attach_screenshot_to_report(file_name):
    allure.attach.file(file_name, attachment_type=allure.attachment_type.PNG)

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Currently available option: chrome"
    )

@pytest.fixture
def browser_selected(request):
    return request.config.getoption("--browser")
