from random import sample


file = open("ex3.txt", "w")
numbers_list = sample(range(0, 100), 100)
for i in numbers_list:
    if (i % 3 == 0) and (i % 6 == 0):
        file.write(f'{i};\n')
file.close()

file = open("ex3.txt", "r")
print(file.read())
file.close()
