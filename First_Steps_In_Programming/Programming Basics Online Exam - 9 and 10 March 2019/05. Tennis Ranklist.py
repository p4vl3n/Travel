from math import floor
tournaments = int(input())
current_score = int(input())
won_points = 0
tournaments_won = 0
for tournament in range(tournaments):
    outcome = input()
    if outcome == "W":
        tournaments_won += 1
        current_score += 2000
        won_points += 2000
    elif outcome == "F":
        current_score += 1200
        won_points += 1200
    elif outcome == "SF":
        current_score += 720
        won_points += 720
average_points = floor(won_points / tournaments)
winning_percentage = tournaments_won / tournaments * 100
print(f"Final points: {current_score}")
print(f"Average points: {average_points}")
print(f"{winning_percentage:.2f}%")
