from math import floor
from math import ceil
days_away = int(input())
food_quantity = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
turtle_food = turtle_food / 1000
food_eaten = (dog_food + cat_food + turtle_food) * days_away
difference = abs(food_eaten - food_quantity)
if food_eaten > food_quantity:
    difference = ceil(difference)
    print(f'{difference} more kilos of food are needed.')
else:
    difference = floor(difference)
    print(f'{difference} kilos of food left.')