#/usr/bin/python

def inventory_cost(filename):
	with open(filename) as FH:
		headers = next(FH)
		total = 0.0
		for line in FH:
			parts = line.split(',')
			quant = int(parts[1])
			price = float(parts[2])
			total += quant*price
	return total

cost = inventory_cost('Data/inventory.csv')
print('Total cost:', cost)
