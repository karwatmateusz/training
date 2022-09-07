a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
count_dict = {}
for elem in a:
    count_dict[elem] = a.count(elem)
print(count_dict)
