import re


given_string = input()
pattern = r"(#|\|)(?P<food>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"
calories = 0

for match in re.finditer(pattern, given_string):
    calories += int(match.group('calories'))
days = calories // 2000
print(f"You have food to last you for: {days} days!")
for match in re.finditer(pattern, given_string):
    food = match.group('food')
    date = match.group('date')
    item_cals = match.group('calories')
    print(f"Item: {food}, Best before: {date}, Nutrition: {item_cals}")