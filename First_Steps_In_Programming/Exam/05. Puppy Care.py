food_in_kg = int(input())
total_grams = food_in_kg * 1000
text = input()
while text != "Adopted":
    food_eaten = int(text)
    total_grams -= food_eaten
    text = input()
if total_grams >= 0:
    print(f'Food is enough! Leftovers: {total_grams} grams.')
else:
    print(f'Food is not enough. You need {abs(total_grams)} grams more.')