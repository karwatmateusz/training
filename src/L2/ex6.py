with open('./src/L2/text.txt', 'r') as file:
    x = file.read()
    print(x)
    file.close()

with open('C:/Users/karwa/PycharmProjects/training/src/L2/text2.txt', 'r') as file:
    x = file.readlines()
    print(f'Ilosc linii to {len(x)}')
    file.close()

if file.closed:
    print("Plik zamkniety")
else: 
    print("Plik dalej otwarty")