from multiprocessing.sharedctypes import Value
import random


class Number:
    def __init__(self, value=random.random()):
        self.value = value

    def __add__(self, other):
        sum = Number(self.value + other.value)
        return sum.value


first_number = Number()
second_number = Number(3)

x = first_number + second_number

print(
    f"Wartosc dodania dwoch wartosci {first_number.value:.2f} i {second_number.value} to: {x:.2f}"
)
