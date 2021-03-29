days = int(input())
players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
water_supply = days * players * water_per_day_per_person
food_supply = days * players * food_per_day_per_person
for day in range(1, days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy > 0:
        if day % 2 == 0:
            group_energy *= 1.05
            water_supply *= 0.70
        if day % 3 == 0:
            group_energy *= 1.10
            food_supply -= food_supply / players
if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_supply:.2f} food and {water_supply:.2f} water.")
