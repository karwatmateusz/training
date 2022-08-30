list = [1, 'jakis', 2, 'tam', 'tekst', 3, 4, 5]

file = open('./src/L2/text4.txt', 'w')
file.write(str(list))
file.write('\n')
file.write('\n')
file.write('cos')
# file.write(f"{list}\ncos")
file.close()
