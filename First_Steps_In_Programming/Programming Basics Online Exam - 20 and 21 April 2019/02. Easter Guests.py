from math import ceil
guest_count = int(input())
budget = float(input())
bread_needed = ceil(guest_count / 3)
bread_cost = 4
eggs_needed = guest_count * 2
egg_cost = 0.45
total_cost = bread_needed * bread_cost + eggs_needed * egg_cost
diff = abs(budget - total_cost)
if budget >= total_cost:
    print(f'Lyubo bought {bread_needed} Easter bread and {eggs_needed} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")