first_workrate = int(input())
second_workrate = int(input())
third_workrate = int(input())
total_people = int(input())
combined_hourly_workrate = first_workrate + second_workrate + third_workrate
hours = 0
while total_people > 0:
    hours += 1
    if hours and hours % 4 == 0:
        pass
    else:
        total_people -= combined_hourly_workrate

print(f"Time needed: {hours}h.")