text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book\n It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged\n It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

file = open('./src/L2/text.txt', 'w')
file.write(text)
file.close()

file = open('./src/L2/text.txt', 'r')
i=0
for line in file:
    i+=1
print(f'Ilosc linii: {i}')

# print(f' Ilosc linii v2 to {len(file.readlines())}')
file.close()