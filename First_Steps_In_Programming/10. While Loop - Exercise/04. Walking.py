daily_target = 10000
daily_steps = 0
target_reached = False

while not target_reached:
    command = input()
    if command == "Going home":
        steps = int(input())
        daily_steps += steps
        if daily_target <= daily_steps:
            target_reached = True
        break
    else:
        steps = int(command)
        daily_steps += steps
    if daily_target <= daily_steps:
        target_reached = True

difference = abs(daily_steps - daily_target)
if not target_reached:
    print(f"{difference} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")


