painted_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
for egg in range(painted_eggs):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1
