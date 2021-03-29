days = int(input())
total_food = float(input())
biscuits = 0
eaten_by_dog = 0
eaten_by_cat = 0
total_food_eaten = 0
for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    eaten_by_dog += dog_food
    eaten_by_cat += cat_food
    total_food_eaten += dog_food + cat_food
    if day % 3 == 0:
        biscuits += 0.10 * (dog_food + cat_food)
print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total_food_eaten / total_food * 100:.2f}% of the food has been eaten.')
print(f'{eaten_by_dog / total_food_eaten * 100:.2f}% eaten from the dog.')
print(f'{eaten_by_cat / total_food_eaten * 100:.2f}% eaten from the cat.')