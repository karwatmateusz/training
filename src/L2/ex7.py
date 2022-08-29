type_counter = {
    'lists': 0,
    'dicts': 0,
    'tuples': 0
}

print(type_counter.keys())

json_values = [[1,2], (1,2), [1,2], (1,2), {'a': 2}]

for element in json_values:
    if type(element) is list:
        type_counter['lists'] += 1
    elif type(element) is dict:
        type_counter['dicts'] += 1
    elif type(element) is tuple:
        type_counter['tuples'] += 1

print(type_counter)