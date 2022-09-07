with open("./src/L2/text.txt", "r") as file:
    x = file.read()
    print(x)

with open("C:/Users/karwa/PycharmProjects/training/src/L2/text2.txt", "r") as file:
    x = file.readlines()
    print(f"Ilosc linii to {len(x)}")

try:
    with open("C:/Users/dsasdsa.txt", "r") as file:
        x = file.readlines()
        print(f"Ilosc linii to {len(x)}")
except FileNotFoundError as e:
    print(e)
