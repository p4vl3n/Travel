budget = float(input())
products_count = 0
total_cost = 0
spent_it_all = False
product = input()
while product != "Stop":
    cost = float(input())
    products_count += 1
    if products_count % 3 == 0:
        cost *= 0.50
    total_cost += cost
    budget -= cost
    if budget < 0:
        spent_it_all = True
        break
    product = input()
if spent_it_all:
    print(f"You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")
else:
    print(f"You bought {products_count} products for {total_cost:.2f} leva.")