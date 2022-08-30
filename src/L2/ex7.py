import json


type_counter = {
    'lists': 0,
    'dicts': 0,
    'tuples': 0
}

# print(type_counter.keys())

# json_values = [[1,2], (1,2), [1,2], (1,2), {'a': 2}]

json_values = {
   "name":"Jack",
   "age":30,
   "contactNumbers":[
      {
         "type":"Home",
         "number":"123 123-123"
      },
      {
         "type":"Office",
         "number":"321 321-321"
      }
   ],
   "spouse": None,
   "favoriteSports":[
      "Football",
      "Cricket"
   ],
   "employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
],
    "firstName": "Rack",
    "lastName": "Jackon",
    "gender": "man",
    "address": {
        "streetAddress": "126",
        "city": "San Jone",
        "state": "CA",
        "postalCode": "394221"
    },
    "phoneNumbers": [
        { "type": "home", "number": "7383627627" }
    ]
}

for element in json_values.values():
    if type(element) is list:
        type_counter['lists'] += 1
    elif type(element) is dict:
        type_counter['dicts'] += 1
    elif type(element) is tuple:
        type_counter['tuples'] += 1

print(type_counter)