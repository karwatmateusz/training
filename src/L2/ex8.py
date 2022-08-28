from random import sample


sample_list = ['k', 'e', 'y']
list2 = ['a','b','c']
conc = [sample_list, list2]
my_dict = dict()

for list in conc:
    my_dict[''.join(list)] = list

# my_dict[''.join(sample_list)] = sample_list

print(my_dict)