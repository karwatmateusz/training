from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

"""OLD fixture with webdriver service+path and driver in request variables"""
# @pytest.fixture(scope="class", autouse=True)
# def driver_setup(request):
#     print("\nSetting up browser")
#     service_object = Service("/Users/MateuszKarwat/webdrivers/chromedriver")
#     driver = webdriver.Chrome(service=service_object)
#     driver.maximize_window()
#     print("\n Browser up and running")
#     request.cls.driver = driver
#     yield driver
#     print("\n Closing browser")
#     # driver.close()


"""New fixture using webdriver manager"""


@pytest.fixture(scope="class", autouse=True)
def driver_setup(request):
    print("\nSetting up browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    print("\nBrowser up and running")
    yield
    print("\nTesting finished \nClosing browser")
    # driver.close()


"""Fixture to take screenshot after test"""


@pytest.fixture(scope="function", autouse=True)
def take_screenshot(request):
    # yield
    # if request.node.rep_call.failed:
    yield
    # Sprawdzic co zwraca request.node
    # if request.node == "call" and request.node.rep_call.failed:
    #     print("screenshot taking")
    #     driver = request.cls.driver
    #     file_name = f'{request.node.name}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace(
    #         "/", "_"
    #     ).replace(
    #         "::", "__"
    #     )
    #     print(f"file name to {file_name}")
    #     driver.save_screenshot(file_name)
    #     print("screenshot saved")
    # else:
    print("test passed")


# @pytest.fixture
# def print_msg():
#     print("I am a fixture running")
#     a = 2
#     yield a
#     print("After function")


# @pytest.fixture(scope="session", autouse=False)
# def print_msg_session():
#     print("\nFixture with session setup")
#     print("Browser set up")
#     yield
#     print("\n \nClearing all data")
#     print("Closing session")


# @pytest.fixture
# def inside_fixture(request):
#     a = request.getfixturevalue("print_msg")
#     print("Inside fixture")
#     # a = 4
#     yield a
#     print("After inside fixture")


# def pytest_addoption(parser):     -> dlaczego nie dziala? Wszystkie opcje w jednej funkcji?
#     parser.addoption(
#         "--some", action="store", default="type1", help="value to print"
#         )

# @pytest.fixture
# def value_to_print2(request):
#     return request.config.getoption("--some")

# def pytest_addoption(parser):
#     parser.addoption(
#         "--value", action="store", default="type1", help="my option: type1 or type2"
#     )

# @pytest.fixture
# def value_to_print(request):
#     return request.config.getoption("--value")
