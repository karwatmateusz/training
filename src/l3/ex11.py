dictionary = {
    "klucz": "asd",
    "cos": "x",
    "ala": "ma",
    "kot": "krotkie",
    "pies": "dlugie",
}


def key_with_longest_value(dictionary):
    max_key = list(dictionary.keys())[0]
    for key in dictionary:
        max_key = key if (len(dictionary[key]) > len(dictionary[max_key])) else max_key
    return max_key


print(key_with_longest_value(dictionary))
