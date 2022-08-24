file = open("ex2.txt", "w")
for i in range(100):
    file.write(f'{i};\n')
file.close()

file = open("ex2.txt", "r")
print(file.read())
file.close()