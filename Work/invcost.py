#/usr/bin/python
import csv
import sys

def inventory_cost(filename):
	with open(filename,'rt') as FH:
		rows = csv.reader(FH)
                headers = next(rows)
		total = 0.0
		for row in rows:
			try:	
				quant = int(row[1])
				price = float(row[2])
				total += quant*price
			except ValueError:
				print('Bad Row', row)
	return total

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/inventory.csv'
cost = inventory_cost(filename)
print('Total cost:', cost)
