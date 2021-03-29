days = int(input())
winning_day = 0
losing_day = 0
pay_per_win = 20
winnings = 0
sport = ""
for day in range(days):
    wins = 0
    losses = 0
    while sport != "Finish":
        sport = input()
        if sport == "Finish":
            break
        outcome = input()
        if outcome == "win":
            wins += 1
        elif outcome == "lose":
            losses += 1
    daily_pay = pay_per_win * wins
    if wins > losses:
        winning_day += 1
        daily_pay *= 1.10
    else:
        losing_day += 1
    winnings += daily_pay
    sport = ""
if winning_day > losing_day:
    winnings *= 1.20
    print(f'You won the tournament! Total raised money: {winnings:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {winnings:.2f}')
