liter_fuel = 2.10
tour_guide = 100
budget = float(input())
needed_fuel = float(input())
day_of_the_week = input()
total_cost = needed_fuel * liter_fuel + tour_guide
if day_of_the_week == "Saturday":
    total_cost *= 0.90
elif day_of_the_week == "Sunday":
    total_cost *= 0.80
difference = budget - total_cost
if difference >= 0:
    print(f'Safari time! Money left: {difference:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(difference):.2f} lv.')
