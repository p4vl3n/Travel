car_race = list(map(int, input().split()))
first_racer = 0
second_racer = 0

for racer_one in range(0, int((len(car_race) - 1)/2)):
    if not car_race[racer_one]:
        first_racer *= 0.8
    else:
        first_racer += car_race[racer_one]

for racer_two in range(len(car_race) - 1, int((len(car_race) - 1)/2), -1):
    if not car_race[racer_two]:
        second_racer *= 0.8
    else:
        second_racer += car_race[racer_two]

if first_racer > second_racer:
    print(f"The winner is right with total time: {second_racer:.1f}")
else:
    print(f"The winner is left with total time: {first_racer:.1f}")