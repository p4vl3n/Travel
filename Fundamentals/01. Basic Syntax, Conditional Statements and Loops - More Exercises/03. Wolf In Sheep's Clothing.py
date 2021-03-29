animals = input().split(", ")
animals.reverse()
wolf_is_first = False
if animals[0] == "wolf":
    print(f"Please go away and stop eating my sheep")
    wolf_is_first = True
if not wolf_is_first:
    for i, position in enumerate(animals):
        if position == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")