flour_price = float(input())
flour_quantity = float(input())
sugar_quantity = float(input())
egg_cartons_count = int(input())
yeast_packs = int(input())
sugar_price = 0.75 * flour_price
egg_carton_price = 1.10 * flour_price
yeast_price = 0.20 * sugar_price
flour_cost = flour_price * flour_quantity
sugar_cost = sugar_price * sugar_quantity
eggs_cost = egg_carton_price * egg_cartons_count
yeast_cost = yeast_price * yeast_packs
total_cost = flour_cost + sugar_cost + eggs_cost + yeast_cost
print(f'{total_cost:.2f}')