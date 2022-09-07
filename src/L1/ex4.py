import csv


header = ['key', 'value']
data = [['apple', 4], ['banana', 4], ['orange', 2]]

file = open("ex4.csv", "w", newline="")
csvwriter = csv.writer(file)
csvwriter.writerow(header)
csvwriter.writerows(data)
file.close()

file = open("ex4.csv", "r")
csvreader = csv.reader(file)
next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()
# print(rows)

dictionary = {
    row[0]: row[1] for row in rows
    }
print(dictionary)
