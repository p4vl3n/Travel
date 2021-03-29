from math import ceil
days = int(input())
first_day_distance = float(input())
total_distance = 0
total_distance += first_day_distance
previous_day = first_day_distance
for day in range(days):
    percentage = int(input())
    daily_distance = percentage / 100 * previous_day + previous_day
    previous_day = daily_distance
    total_distance += daily_distance
diff = abs(1000 - total_distance)
if total_distance >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")