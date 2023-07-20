import random
import csv

rfq = []

def generate_multi_legged_rfq():
    row = []
    product = 'product '
    price = 'price '
    quantity = 'quantity '
    for i in range(300):
        for j in [product, price, quantity]:
            for _ in range(random.randrange(1, 3)):
                string = 'RFQ ' + str(i) + ' ' + j + ' ' + str(random.randint(1, 100))
                row.append(string)
        rfq.append(row)
        row = []
        product = 'product '
        price = 'price '
        quantity = 'quantity '

generate_multi_legged_rfq()

with open('junk.csv', 'w') as file:
    for row in rfq:
        print(row)
        writer = csv.writer(file)
        writer.writerow(row)
