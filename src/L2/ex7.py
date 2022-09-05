import json


type_counter = {"lists": 0, "dicts": 0, "tuples": 0}

with open("src\L2\data.json", "r") as file_data:
    json_data = json.load(file_data)


for element in json_data.values():
    if type(element) is list:
        type_counter["lists"] += 1
    elif type(element) is dict:
        type_counter["dicts"] += 1
    elif type(element) is tuple:
        type_counter["tuples"] += 1

print(type_counter)
