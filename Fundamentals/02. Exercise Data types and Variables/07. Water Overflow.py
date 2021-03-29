poured_water = 0
tank_capacity = 255
lines = int(input())
for line in range(lines):
    water_pour = int(input())
    if tank_capacity >= water_pour:
        tank_capacity -= water_pour
        poured_water += water_pour
    else:
        print(f"Insufficient capacity!")
print(poured_water)