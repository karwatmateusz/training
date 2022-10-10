import pytest


@pytest.fixture
def suite_fixture():
    print("\nFixture 2 running")
    yield 'something'


# @pytest.fixture
# def inner_fixture(suite_fixture):
#     print("I am inner fixture")
#     print(suite_fixture)
#     print("Closing inner fixture")


@pytest.fixture
def return_value():
    print('inner fixture')
    yield 10
    print('closing inner fixture')

# @pytest.fixture
# def print_value(return_value):
#     print('outer fixture')
#     a, b = return_value
#     print(f'wartosc to {a} {b}')
#     yield a
#     print('closing outer fixture')
# czym się różnią /\ i \/?
@pytest.fixture()
def inside_fixture(request):
    a = request.getfixturevalue("return_value")
    print('outer fixture')
    print(f'wartosc to {a}')
    yield a
    print('closing outer fixture')
    