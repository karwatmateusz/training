import pytest

# //mark.parametrize\
# // podział na kilka folderów z testami - test_suite_1 / test_suite_2, oba po jednym teście + conftest.py dla każdego
# //session scope
# // session = BEFORE suite/AFTER
# // function = before each
# // fixture + yield
# // fixture + fixture inside (fixture request) DONE
# creat fixtures for selenium setup

@pytest.mark.smoke
@pytest.mark.parametrize("inputX, inputY, expected", [(1, 2, 3), (1, 10, 11)])
def test_add(inputX, inputY, expected):
    print(f"parametry funkcji to: {inputX}, {inputY}, a spodziewamy się {expected}")
    a = inputX
    b = inputY
    result = expected
    assert a+b == result, f'test failed wrong adding, should be {expected}, was {inputX+inputY}'

@pytest.mark.parametrize("inputX", (1, 2, 3, 4))
@pytest.mark.parametrize("inputY", (0, 1, 2, 4))
@pytest.mark.smoke
def test_sub(inputX, inputY):
    print(f"zestaw danych to X: {inputX} Y: {inputY}")
    a = inputX
    b = inputY
    result = a-b
    assert a-b == result, 'substraction, test failed'
