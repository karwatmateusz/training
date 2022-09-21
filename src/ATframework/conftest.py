import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class", autouse=True)
def driver_setup(request):
    print("\nSetting up browser")
    service_object = Service("/Users/MateuszKarwat/webdrivers/chromedriver")
    driver = webdriver.Chrome(service=service_object)
    driver.maximize_window()    
    # driver.get("https://demo.opencart.com/index.php?route=account/login")
    # driver.find_element(By.CSS_SELECTOR, '#input-email')
    print("\n Browser up and running")
    request.cls.driver = driver
    yield driver
    print("\n Closing browser")
    # driver.close()

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