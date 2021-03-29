minutes_a_walk = int(input())
walks_a_day = int(input())
calorie_intake = int(input())
burned_calories = walks_a_day * minutes_a_walk * 5
if burned_calories >= 0.50 * calorie_intake:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')