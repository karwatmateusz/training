import random


class Number:
    def __init__(self, value=random.random()) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, other):
        sum = self.value + other.value
        return sum

    def __radd__(self, other):
        sum = self.value + other
        return sum


list = []

for i in range(5):
    list.append(Number(i))

x = sum(list)
print(f" Suma listy to {x}")
