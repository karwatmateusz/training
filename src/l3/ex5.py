string_list = ['warszawa', 'lublin', 'wroclaw', 'pojazd','samochod', 'kuchenka','lodowka','telewizor','suszarka','auto']


"""Zadanie a: len >= 3 i <=7"""
# for x in string_list:
#     if (len(x)>=3 and len(x)<=7):
#         print(x)

# print(list([x for x in string_list if (len(x)>=3 and len(x)<=7)]))

"""Zadanie b: sort alfabetycznie"""
string_list.sort()
print(f"alfabetycznie lista: {string_list}")

"""Zadanie c: sort po len"""
def list_length(list):
    return len(list)

string_list.sort(key=list_length)
print(f"lista po dlugosci to: {string_list}")

"""Zadanie d: c tylko odwrotnie"""
string_list.sort(key=list_length, reverse=True)
print(f"odwrotnie lista niz c: {string_list}")