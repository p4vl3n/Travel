sea_packages = int(input())
mountain_packages = int(input())
profit = 0
command = input()
sold_out = False
while command != "Stop":
    if command == "sea":
        if sea_packages == 0:
            pass
        else:
            sea_packages -= 1
            profit += 680
    elif command == "mountain":
        if mountain_packages == 0:
            pass
        else:
            mountain_packages -= 1
            profit += 499
    if sea_packages == 0 and mountain_packages == 0:
        sold_out = True
        break
    command = input()
if sold_out:
    print(f"Good job! Everything is sold.")
print(f"Profit: {profit} leva.")