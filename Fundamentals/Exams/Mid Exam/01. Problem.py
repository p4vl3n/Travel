orders = int(input())
total_price = 0
for order in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())
    order_cost = days * capsules_count * capsule_price
    total_price += order_cost
    print(f"The price for the coffee is: ${order_cost:.2f}")
print(f"Total: ${total_price:.2f}")
