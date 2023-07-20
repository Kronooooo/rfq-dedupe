import csv

rows = []

with open('junk.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        for i in range(len(row)):
            rows.append(row)


with open('normalized.csv', 'w') as file:
    for row in rows:
        writer = csv.writer(file)
        writer.writerow(row)