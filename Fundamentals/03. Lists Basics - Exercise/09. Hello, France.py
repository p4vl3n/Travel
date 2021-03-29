given_input = input().split("|")
type_and_price = [x.split("->") for x in given_input]
capital = float(input())
starting_budget = capital
clothes = 50
shoes = 35
accessories = 20.50
ticket_target = 150
sales = 0
original_price = []
selling_price = []
for i, product in enumerate(type_and_price):
    if product[0] == "Clothes" and capital >= float(product[1]):
        if float(product[1]) <= clothes:
            capital -= float(product[1])
            sales += float(product[1]) + 0.40 * float(product[1])
            original_price.append(float(product[1]))
            selling_price.append(float(product[1]) + 0.40 * float(product[1]))
    elif product[0] == "Shoes" and capital >= float(product[1]):
        if float(product[1]) <= shoes:
            capital -= float(product[1])
            sales += float(product[1]) + 0.40 * float(product[1])
            original_price.append(float(product[1]))
            selling_price.append(float(product[1]) + 0.40 * float(product[1]))
    elif product[0] == "Accessories" and capital >= float(product[1]):
        if float(product[1]) <= accessories:
            capital -= float(product[1])
            sales += float(product[1]) + 0.40 * float(product[1])
            original_price.append(float(product[1]))
            selling_price.append(float(product[1]) + 0.40 * float(product[1]))
profit = sales - sum(original_price)
for i in range(len(selling_price)):
    print(f"{selling_price[i]:.2f}", end=" ")
    if i + 1 == len(selling_price):
        print()
print(f"Profit: {profit:.2f}")
if profit + starting_budget >= ticket_target:
    print(f"Hello, France!")
else:
    print(f"Time to go.")