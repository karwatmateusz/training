import random


random_list = [random.randint(100,200) for i in range (50)]

"""Zadanie a: min i max"""
print("<<<Zadanie a>>>")
print(f"min to {min(random_list)}")
print(f"max to {max(random_list)}")

"""Zadanie b: suma wszystkich elementów"""
print("<<<Zadanie b>>>")
suma = 0
for i in random_list:
    suma += i
print(f"suma to {suma}")
# print(sum(random_list))

"""Zadanie c: zwróć i usuń ostatni element"""
print(f"ostatni element przed modyfikacją to {random_list[-1]}")
last_elem = random_list.pop()
print(f"ostatni element to {last_elem}")

"""Zadanie d: wypisz ilosc elementów w liście"""
print(f'Dlugosc list to {len(random_list)}')
