import difflib
from typing import Optional


def ex6():
    tuples_list = [(4, 5), (6, 1), (4, 5), (6, 1)]
    print(set(tuples_list))


def ex7():
    number_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

    # first method with collections
    from collections import Counter

    print(Counter(number_list))

    # second method
    counter = dict()
    for n in number_list:
        counter[n] = number_list.count(n)
    print(counter)


def ex8(length: int = 10):
    # method using random.sample
    from random import choice, sample
    from string import ascii_letters

    # first method
    print("".join(sample(ascii_letters, length)))
    # second method
    print("".join(choice(ascii_letters) for _ in range(length)))


def rand_list(count: int = 0) -> list:
    from random import randint

    return [randint(100, 200) for _ in range(count)]


def rand_string(length: int = 0) -> str:
    from random import sample
    from string import ascii_letters

    return "".join(sample(ascii_letters, length))


def ex9() -> dict:
    from random import randint

    lists_len = 5
    key_len = 5
    value_len = 3, 9
    keys_list = [rand_string(key_len) for _ in range(lists_len)]
    values_list = [rand_string(randint(*value_len)) for _ in range(lists_len)]
    # first
    output_dict = dict()
    for k, v in zip(keys_list, values_list):
        output_dict[k] = v
    print(output_dict)

    # second
    print(output_dict := {k: v for k, v in zip(keys_list, values_list)})
    return output_dict
ex9()


def ex9m():
    import random
    import string

    def generate_random_dict(length):
        random_dict = {}
        for _ in range(length):
            rand_key = "".join(random.sample(string.ascii_letters + string.digits, k=5))
            rand_value = "".join(
                random.sample(
                    string.ascii_letters + string.digits, k=random.randint(a=3, b=9)
                )
            )
            random_dict[rand_key] = rand_value
        return random_dict

    dictionary = generate_random_dict(3)
    print(dictionary)
ex9m()

def ex10():
    from copy import copy

    input_dict = ex9()
    input_dict2 = copy(input_dict)

    # first
    for k, v in input_dict.items():
        input_dict[k] = len(v)
    print(input_dict)

    # second
    print({k: len(v) for k, v in input_dict.items()})


def ex11():
    input_dict = ex9()

    # first
    maximum = max(input_dict.values(), key=len)
    key_with_max_val = None
    for k, v in input_dict.items():
        if v == maximum:
            key_with_max_val = k
            break
    print(key_with_max_val)

    # second
    anonymous = lambda x: len(input_dict[x])

    def my_func(x):
        return len(input_dict[x])

    print(max(input_dict, key=anonymous))
    print(max(input_dict, key=my_func))


def ex12() -> dict:
    input_dict = ex9()
    dictionary = input_dict
    dictionary = {k: len(v) for k, v in dictionary.items()}
    print(output := dict(sorted(dictionary.items(), key=lambda item: item[1])))
    return output


def ex13():
    input_dict = ex12()
    print(f"dict: {input_dict}")
    # first
    print({k: v**2 for k, v in input_dict.items()})
    # second
    print(dict(map(lambda x: (x[0], x[1]**2), input_dict.items())))


# OOP

def ex1_oop():

    def zero_checker(func):
        def wrapper(*args):
            if args[1] == 0:
                raise ZeroDivisionError("Pamiętaj cholero nie dziel przez zero!")
            return func(*args)
        return wrapper

    @zero_checker
    def divide(a, b):
        return a / b

    print(divide(2, 1))
    print(divide(2, 0))


# 2 OOP

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} lat {self._age}"

    def __repr__(self) -> str:
        return f"{self.__class__} - {self._name} - {self._age}"

    def new_name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def name(self) -> str:
        return f"{self._name}"

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name


def ex2_oop():
    print(p := Person("maciej", 2))
    p.name = "dupa"
    print(p)


from random import randint


class Number:
    def __init__(self, value: Optional = None):
        self.value = value if value else randint(0, 50)

    def __repr__(self) -> str:
        return f"{self.value}"

    def __add__(self, other):
        if isinstance(other, int):
            return self.__class__(self.value + other)
        return self.__class__(self + other.value)

    def __radd__(self, other):
        return self.__class__(self.value + other)


def ex4_oop():
    n1, n2 = Number(), Number()
    print(n1 + n2)
    print(type(n1 + n2))
    print(n1 + 2)
    print(2 + n1)
    print(sum([n1, n2]))


# ex4_oop()

# from concurrent.futures import ProcessPoolExecutor
# with ProcessPoolExecutor(max_workers=3) as executor:
#     # executor.map(func, [1,2,3,4,5,])
#     future_list = [executor.submit(func, j) for j in jobs]
#     result_list = [f.result() for f in future_list]

#
