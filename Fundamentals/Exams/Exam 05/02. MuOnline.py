health = 100
bitcoins = 0
given_string = input().split("|")
made_it = True
for number, room in enumerate(given_string):
    action, blood = room.split()
    if action == "potion":
        if int(blood) + health > 100:
            healed = 100 - health
            print(f"You healed for {healed} hp.")
            health = 100
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {blood} hp.")
            health += int(blood)
            print(f"Current health: {health} hp.")
    elif action == "chest":
        print(f"You found {blood} bitcoins.")
        bitcoins += int(blood)
    else:
        if health - int(blood) > 0:
            health -= int(blood)
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {number + 1}")
            made_it = False
            break
if made_it:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")