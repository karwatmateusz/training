import logging
import pytest


@pytest.fixture
def suite_fixture():
    print("\nFixture 1 running")


@pytest.fixture(scope="function", autouse=False)
def print_msg_function():
    print("I am a fixture running for particular function")
    print("Setting test data")
    yield
    print("\nClosing function")
    print("Clearing all data")



@pytest.fixture(params=[("one", "one two"), ("two")])
def param_fix(request):
    print(f' parametry to {request.param}')