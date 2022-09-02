list = [1, 2, 3, 4, 5]


def list_square(list):
    list_squared = [x * 2 for x in list]
    return list_squared


print(list_square(list))
