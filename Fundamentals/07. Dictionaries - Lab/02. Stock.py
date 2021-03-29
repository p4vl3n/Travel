products = input().split()
bakery = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i + 1])
    bakery[key] = value

searching_for = input().split()

for product in searching_for:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
