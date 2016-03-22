

def read_into_dict(filename):
	'''
	reads all the grocery stuff
	returns dict of prices and products (key) 
	'''

	f = open(filename, 'r')
	lines = f.readlines() 


	prices = {} 

	for i in range(len(lines)):
		line = lines[i]
		line = line[:-1]
		pro_price = line.split(" ")
		product = pro_price[0]
		cost = float(pro_price[1])
		prices[product] = cost

	return prices 

def calc_cost(prices, receipt): 
	'''
	We want to compute the cost of each sale. Write a function calc_cost that takes in two dictionaries:

    prices - a dict mapping each product to the single unit price
    receipt - a dict mapping each product in a sale to the quantity

	and returns a float with the total sale cost.
	'''

	total_cost = 0 

	for item in receipt:
		quantity = receipt[item]
		unit_price = prices[item]
		total_cost += quantity * unit_price

	return total_cost

def process_receipt(prices, receipt): 
	test_receipt = read_into_dict(receipt)
	total_sale = calc_cost(prices, test_receipt)
	print(total_sale)

