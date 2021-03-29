juniors = int(input())
seniors = int(input())
race_type = input()
participants = juniors + seniors
juniors_entry_fee = 0
seniors_entry_fee = 0
if race_type == "trail":
    juniors_entry_fee = 5.50
    seniors_entry_fee = 7
elif race_type == "cross-country":
    if participants >= 50:
        juniors_entry_fee = 0.75 * 8
        seniors_entry_fee = 0.75 * 9.50
    else:
        juniors_entry_fee = 8
        seniors_entry_fee = 9.50
elif race_type == "downhill":
    juniors_entry_fee = 12.25
    seniors_entry_fee = 13.75
elif race_type == "road":
    juniors_entry_fee = 20
    seniors_entry_fee = 21.50
collected_sum = juniors * juniors_entry_fee + seniors * seniors_entry_fee
donation = 0.95 * collected_sum
print(f'{donation:.2f}')