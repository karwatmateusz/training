import pytest


# @pytest.mark.suite2
# @pytest.mark.smoke
# def test_suite2(inner_fixture):
#     print("Suite 2 test running")


@pytest.mark.suite2
def test_fix(inside_fixture):
    print("starting test")
    a = inside_fixture
    print(f' wartosc w tescie to {a}')
    print("test finished")

@pytest.mark.testoption
def test_option_print(value_to_print):
    print(f'\nwartosc z wiersza polecen to {value_to_print}')
