from math import floor
party_size = int(input())
current_party = party_size
total_companions = party_size
days = int(input())
profit = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        current_party -= 2
    if day % 15 == 0:
        current_party += 5
    profit += 50
    profit -= 2 * current_party
    if day % 3 == 0:
        profit -= 3 * current_party
    if day % 5 == 0:
        profit += 20 * current_party
    if day % 3 == 0 and day % 5 == 0:
        profit -= 2 * current_party
coin_per_companion = floor(profit / current_party)
print(f"{current_party} companions received {coin_per_companion} coins each.")