import re


text = input()
pattern = r"(^|\s)>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
total_spent = 0
furniture = []

while not text == "Purchase":
    match = re.match(pattern, text)
    if match:
        order = match.groupdict()
        total_spent += float(order['price']) * int(order['quantity'])
        name_of_furniture = order['furniture']
        furniture.append(name_of_furniture)
    text = input()
print("Bought furniture:")
if furniture:
    print("\n".join(furniture))
print(f"Total money spend: {total_spent:.2f}")