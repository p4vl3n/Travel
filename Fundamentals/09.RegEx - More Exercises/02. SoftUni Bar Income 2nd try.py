import re

name_pattern = r"(?<=\%)(?P<name>[A-Z][a-z]+)(?=\%)"
product_pattern = r"(?<=\<)(?P<product>[a-zA-Z]+)(?=\>)"
quantity_pattern = r"(?<=\|)(?P<quantity>\d+)(?=\|)"
price_pattern = r"(?P<price>[\d]+(\.[\d]+)?)(?=\$)"

total_order = 0
text = input()
while not text == "end of shift":
    match_name = re.search(name_pattern, text)
    match_product = re.search(product_pattern, text)
    match_quantity = re.search(quantity_pattern, text)
    match_price = re.search(price_pattern, text)
    if match_name and match_product and match_quantity and match_price:
        name = match_name.group('name')
        product = match_product.group('product')
        quantity = int(match_quantity.group('quantity'))
        price = float(match_price.group('price'))
        order = quantity * price
        total_order += order
        print(f"{name}: {product} - {order:.2f}")
    text = input()
print(f"Total income: {total_order:.2f}")