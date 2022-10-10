import pytest


@pytest.mark.suite1
@pytest.mark.smoke
def test_suite1(suite_fixture, print_msg_function):
    print("Suite 1 test running")
    assert 2 == 4, f'test failed here'

@pytest.mark.suite1
def test_param(param_fix):
    print("param fixture")