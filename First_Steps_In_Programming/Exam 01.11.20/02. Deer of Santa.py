from math import floor
from math import ceil
days_santa_is_gone = int(input())
left_food = int(input())
rudolph_food = float(input())
vixen_food = float(input())
dasher_food = float(input())
food_eaten_per_day = rudolph_food + vixen_food + dasher_food
total_food_eaten = days_santa_is_gone * food_eaten_per_day
diff = abs(left_food - total_food_eaten)
if total_food_eaten > left_food:
    print(f"{ceil(diff)} more kilos of food are needed.")
else:
    print(f"{floor(diff)} kilos of food left.")