ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
allowed_quantity = int(input())
days_till_xmas = int(input())
xmas_spirit = 0
total_cost = 0
for day in range(1, days_till_xmas + 1):
    if day % 11 == 0:
        allowed_quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set * allowed_quantity
        xmas_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * allowed_quantity
        xmas_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights * allowed_quantity
        xmas_spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        xmas_spirit += 30
    if day % 10 == 0:
        total_cost += tree_skirt + tree_garlands + tree_lights
        xmas_spirit -= 20
    if day % 10 == 0 and day == days_till_xmas:
        xmas_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {xmas_spirit}")

