#/usr/bin/python
import sys

def inventory_cost(filename):
	with open(filename,'rt') as FH:
		headers = next(FH)
		total = 0.0
		for line in FH:
			parts = line.split(',')
			quant = int(parts[1])
			price = float(parts[2])
			total += quant*price
	return total

cost = inventory_cost(sys.argv[1])
print('Total cost:', cost)
