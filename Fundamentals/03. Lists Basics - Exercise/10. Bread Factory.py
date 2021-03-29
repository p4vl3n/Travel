given_list = input().split("|")
events = [x.split("-") for x in given_list]
coins = 100
energy = 100
day_is_complete = True
for i, event in enumerate(events):
    if event[0] == "rest":
        if energy + int(event[1]) > 100:
            gained_energy = 100 - energy
            print(f"You gained {gained_energy} energy.")
            energy = 100
            print(f"Current energy: {energy}.")
        else:
            energy += int(event[1])
            print(f'You gained {int(event[1])} energy.')
            print(f'Current energy: {energy}.')
    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += int(event[1])
            print(f"You earned {event[1]} coins.")
        else:
            print(f"You had to rest!")
            energy += 50
    else:
        if coins > int(event[1]):
            coins -= int(event[1])
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            day_is_complete = False
            break
if day_is_complete:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")