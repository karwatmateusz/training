from random import sample


sample_list = ['k', 'e', 'y']
list2 = ['a','b','c']
conc = [sample_list, list2]
my_dict = dict()

for l in conc:
    my_dict[''.join(l)] = l

print(my_dict)

ll = ["Asd", "dsa", "fgf"]
print({e: list(e) for e in ll})

