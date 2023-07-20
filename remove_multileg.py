import csv
from tokenize_rfq import *

rows = []
single_leg = []
dict = {}

# This removes all multi-leg

with open('junk.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        rows.append(row)


for row in rows:
    rfq = tokenize_rfq(row)
    for field in rfq:
        if not field[1] in dict:
            dict[field[1] + field[2]] = field[3]


# with open('single-leg.csv', 'w') as file:
#     writer = csv.writer(file)
#     for row in rows:
#         writer.writerow(row)

with open('mycsvfile.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.writer(f)
    w.writerows(dict.items())