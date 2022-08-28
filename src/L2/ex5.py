try:
    file = open('./src/L2/text5.txt', 'r')
    file.read()
except FileNotFoundError:
    print("Plik nie istnieje")

