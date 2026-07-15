products = {
    "Mobile": 15000,
    "Mouse": 400,
    "Keyboard": 700,
    "Pen": 50,
    "Monitor": 8000
}

for product, price in products.items():
    if price > 500:
        print(product, price)