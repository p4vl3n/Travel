days = int(input())
total_food = float(input())
dog_food = 0
cat_food = 0
total_biscuits = 0
for day in range(1, days + 1):
    food_eaten_by_dog = float(input())
    dog_food += food_eaten_by_dog
    food_eaten_by_cat = float(input())
    cat_food += food_eaten_by_cat
    if day % 3 == 0:
        biscuits = 0.10 * (food_eaten_by_cat + food_eaten_by_dog)
        total_biscuits += biscuits
eaten_food = dog_food + cat_food
percentage_total = eaten_food * 100 / total_food
percentage_dog = (dog_food * 100) / eaten_food
percentage_cat = (cat_food * 100) / eaten_food
print(f"Total eaten biscuits: {biscuits} gr.")
print(f"{percentage_total:.2f}% of the food has been eaten.")
print(f"{percentage_dog:.2f}% eaten from the dog.")

