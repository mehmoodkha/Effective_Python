#/usr/bin/python
import csv
import sys

def read_inventory(filename):
    inventory = list()

    with open(filename, 'rt') as FH:
        rows = csv.reader(FH)

        headers = next(rows)
        for row in rows:
            prod = dict()
            prod['name'] = row[0]
            prod['quant'] = int(row[1])
            prod['price'] = float(row[2])
            inventory.append(prod)

    return inventory

def read_prices(filename):
    prices = dict()
    with open(filename,'rt') as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        for row in rows:

            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue
    return prices

def make_report(products, prices):
	values = list()
	
       	for prod in products:
		name = prod['name']
		quant = prod['quant']
		price = prod['price']
		latest_price = prices[name]
		values.append( (name, quant, latest_price, latest_price - price) )

	return values

	

inventory = read_inventory('Data/inventory.csv')

prices = read_prices('Data/prices.csv')

totalcost = 0.0
for prod in inventory:
    totalcost += prod["quant"]*prod["price"]

print("total=", totalcost)

presentvalue = 0.0
for product in inventory:
    presentvalue += product["quant"] * prices[product["name"]]
print("PresentValue", presentvalue)

Gain=presentvalue-totalcost
print(Gain)

report = make_report(inventory, prices)

for row in report:
	print(row)

#print("Inventroy Items", inventory)
# print("Inventory Items")
# from pprint import pprint
# pprint(inventory)
# pprint(prices)

#commit 3 different price.
