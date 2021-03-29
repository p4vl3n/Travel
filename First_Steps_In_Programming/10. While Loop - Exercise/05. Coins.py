change = float(input())
change *= 100
change = int(change)
coin_count = 0
while change >= 1:
    coin_count += 1
    if change // 200 >= 1:
        change -= 200
    elif change // 100 >= 1:
        change -= 100
    elif change // 50 >= 1:
        change -= 50
    elif change // 20 >= 1:
        change -= 20
    elif change // 10 >= 1:
        change -= 10
    elif change // 5 >= 1:
        change -= 5
    elif change // 2 >= 1:
        change -= 2
    elif change == 1:
        change -= 1

print(coin_count)
