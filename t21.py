prices = []

for i in range(5):
    price = float(input("Enter Price: "))
    prices.append(price)

highest = prices[0]

for price in prices:
    if price > highest:
        highest = price

print("Prices:", prices)
print("Highest Price:", highest)