locations = int(input())
for mine in range(locations):
    expected_average_mine = float(input())
    days_to_mine = int(input())
    total_mine = 0
    for day in range(days_to_mine):
        daily_mine = float(input())
        total_mine += daily_mine
    average_daily_mine = total_mine / days_to_mine
    diff = abs(expected_average_mine - average_daily_mine)
    if expected_average_mine <= average_daily_mine:
        print(f"Good job! Average gold per day: {average_daily_mine:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")