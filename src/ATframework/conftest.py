import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="class", autouse=True)
def driver_setup(request):
    print("\nSetting up browser")
    service_object = Service("/Users/MateuszKarwat/webdrivers/chromedriver")
    driver = webdriver.Chrome(service=service_object)
    driver.maximize_window()    
    print("\n Browser up and running")
    request.cls.driver = driver
    yield
    print("\n Closing browser")
    driver.close()

# @pytest.fixture
# def print_msg():
#     print("I am a fixture running")
#     a = 2
#     yield a
#     print("After function")
    

@pytest.fixture(scope="session", autouse=False)
def print_msg_session():
    print("\nFixture with session setup")
    print("Browser set up")
    yield
    print("\n \nClearing all data")
    print("Closing session")



# @pytest.fixture
# def inside_fixture(request):
#     a = request.getfixturevalue("print_msg")
#     print("Inside fixture")
#     # a = 4
#     yield a
#     print("After inside fixture")
    