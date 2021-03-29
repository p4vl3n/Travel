lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_cost = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        total_cost += helmet_price
    if fight % 3 == 0:
        total_cost += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        total_cost += shield_price
    if fight % 12 == 0:
        total_cost += armor_price
print(f"Gladiator expenses: {total_cost:.2f} aureus")
