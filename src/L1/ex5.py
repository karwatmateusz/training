import csv


file = open("ex6.csv", "r")
csvreader = csv.reader(file)
next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

print(rows)
file.close()
