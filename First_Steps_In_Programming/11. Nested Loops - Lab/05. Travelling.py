destination = input()
while destination != "End":
    needed_money = int(input())
    saved_money = 0
    while saved_money < needed_money:
        saved_money += int(input())
        if saved_money >= needed_money:
            print(f'Going to {destination}!')
    destination = input()
