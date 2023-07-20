import csv

# This splits the rfq into multiple rows

# This is the list of rfqs, should be no duplicates
rows = []

# This is where the split rfq is stored
new_rows = []

def tokenize_rfq(rfq):
    row = []
    for field in rfq:
        row.append(field.split())
    
    return row

with open('junk.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        rows.append(row)


for row in rows:
    new_rows.append(tokenize_rfq(row))

with open('rfq_table.csv', 'w') as file:
    writer = csv.writer(file)
    for row in new_rows:
        for field in row:
            writer.writerow(field)