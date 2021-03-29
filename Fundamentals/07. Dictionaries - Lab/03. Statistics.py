products = {}
command = input()
while not command == "statistics":
    product, quantity = command.split(": ")
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)
    command = input()
print(f"Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
