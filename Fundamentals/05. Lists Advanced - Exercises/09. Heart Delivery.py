current_position = 0
house_counter = 0


def jump(lst, pos, jmp, cntr):
    if pos + jmp >= len(lst):
        pos = 0
        if not lst[pos]:
            return print(f"Place {pos} already had Valentine's day.")
        lst[pos] -= 2
        return
    pos += jmp
    if not lst[pos]:
        return print(f"Place {pos} already had Valentine's day.")
    lst[pos] -= 2
    if not lst[pos]:
        cntr += 1
        return print(f"Place {pos} has Valentine's day.")
    return


neighborhood = list(map(int, input().split("@")))
command = input()

while not command == "Love!":
    command_data = command.split()
    jump_dist = int(command_data[1])
    jump(neighborhood, current_position, jump_dist, house_counter)
    command = input()

print(neighborhood)
print(house_counter)
