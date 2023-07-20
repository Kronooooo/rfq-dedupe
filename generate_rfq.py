import random
import csv
import string
from numpy import choice

max_length = 10
rows = []
weights = [75, 15, 10]

for i in range(100):
    row = []
    field = ''
    num_fields = random.randrange(5, 10)
    for i in range(num_fields):
        
        row.append(random.choice(string.ascii_lowercase))
    
    for i in range(num_fields):
        rows.append(row)
    
with open('test.csv', 'w') as file:
    for row in rows:
        writer = csv.writer(file)
        writer.writerow(row)