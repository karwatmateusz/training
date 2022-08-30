from random import randint


file = open("ex1.txt", "w")
for i in range(100):
    file.write(f"{randint(0, 100)};")
file.close()

file = open("ex1.txt", "r")
print(file.read())
file.close()
