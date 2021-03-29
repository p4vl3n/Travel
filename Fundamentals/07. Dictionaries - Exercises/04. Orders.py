total_order = {}
command = input()
while not command == "buy":
    cmd_data = command.split()
    drink = cmd_data[0]
    price = float(cmd_data[1])
    quantity = int(cmd_data[2])
    if drink not in total_order:
        total_order[drink] = {'price': 0, 'quantity': 0}
        total_order[drink]['price'] = price
        total_order[drink]['quantity'] = quantity
    else:
        if not price == total_order[drink]['price']:
            total_order[drink]['price'] = price
            total_order[drink]['quantity'] += quantity

    command = input()
for drink, value in total_order.items():
    print(f"{drink} -> {value['price']*value['quantity']:.2f}")