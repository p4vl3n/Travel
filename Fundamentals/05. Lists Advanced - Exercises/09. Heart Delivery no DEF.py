neighborhood = list(map(int, input().split("@")))
command = input()
house_counter = 0
position = 0

while not command == "Love!":
    command_data = command.split()
    jump = int(command_data[1])
    if position + jump >= len(neighborhood):
        position = 0
        if not neighborhood[position]:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighborhood[position] -= 2
            if not neighborhood[position]:
                house_counter += 1
                print(f"Place {position} has Valentine's day.")

    else:
        position += jump
        if not neighborhood[position]:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighborhood[position] -= 2
            if not neighborhood[position]:
                house_counter += 1
                print(f"Place {position} has Valentine's day.")
    command = input()

failed_houses = len(neighborhood) - house_counter
print(f"Cupid's last position was {position}.")
if not failed_houses:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")
