file = open("ex3.txt", "w")
for i in range(100):
    if (i%3==0 ) and (i%6==0):
        file.write(f'{i};\n')
file.close()

file = open("ex3.txt", "r")
print(file.read())
file.close()