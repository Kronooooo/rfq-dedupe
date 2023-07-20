import csv

rows = []

def remove_duplicates(c):
    with open(c, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if not (row in rows):
                rows.append(row)
            

remove_duplicates('test.csv')
print(rows)

with open('output.csv', 'w') as file:
    for row in rows:
        writer = csv.writer(file)
        writer.writerow(row)