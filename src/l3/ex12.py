from operator import itemgetter

dictionary = {"abc": 7, "abd": 5, "abz": 1}


# first simple solution
def sort_dict(dictionary):
    sorted_keys = sorted(dictionary, key=dictionary.get)
    new_sorted_dict = {}
    for sorted_elem in sorted_keys:
        new_sorted_dict[sorted_elem] = dictionary[sorted_elem]
    return new_sorted_dict


# second solution
def sort_dict_simple(dictionary):
    new_sorted_dict = dict((sorted(dictionary.items(), key=itemgetter(1))))
    return new_sorted_dict


print(sort_dict(dictionary))
print(sort_dict_simple(dictionary))
