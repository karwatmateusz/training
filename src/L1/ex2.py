from random import randint


file = open("ex2.txt", "w")
for i in range(100):
    file.write(f'{randint(0, 100)}\n')
file.close()

file = open("ex2.txt", "r")
print(file.read())
file.close()
