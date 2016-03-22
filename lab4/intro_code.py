names = ['Alice', 'Bob', 'Charlie']
print(names[1])

prices = {'Apple': .89, 'Banana': .39, 'Bread': 2.50}
print(prices['Banana'])
if ('Chocolate' in prices):
    print(prices['Chocolate'])
else:
    print("No Chocolate!")
prices['Chocolate'] = 1.50
print(list(prices.keys()))
print(list(prices.values()))
print(list(prices.items()))
for product in prices:
    price = '$' + str(prices[product])
    print(product + ' costs ' + price)

filename = 'trial.txt'
f = open(filename, 'r')
lines = f.readlines()
print(lines)
f.close()

