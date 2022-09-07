import csv

students = [
    {"Student": "Jarek", "Wiek": 14, "Miejsce": "Srodek", "Klasa": 7, "Ocena": 4},
    {"Student": "Marek", "Wiek": 13, "Miejsce": "Przod", "Klasa": 6, "Ocena": 2},
]

header = list(students[0].keys())
# print(header)
data = []
for student in students:
    data.append(list(student.values()))
# print(data)
file = open("ex6.csv", "w", newline="")
csvwriter = csv.writer(file)
csvwriter.writerow(header)
csvwriter.writerows(data)
file.close()
