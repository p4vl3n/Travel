def index_is_valid(trgt, ind):
    if 0 <= index < len(trgt):
        return True
    return False


def shoot(trgt, ind, power):
    if index_is_valid(trgt, ind):
        trgt[ind] -= power
        if trgt[ind] <= 0:
            trgt.pop(ind)


def add(trgt, ind, val):
    if index_is_valid(trgt, ind):
        trgt.insert(ind, val)
        return
    return print(f"Invalid placement!")


def strike(trgt, ind, rad):
    if index_is_valid(trgt, ind):
        if ind + rad >= len(trgt) or ind - rad < 0:
            return print(f"Strike missed!")
        else:
            del trgt[ind - rad:ind + rad + 1]


target = list(map(int, input().split()))
command = input()
while not command == "End":
    command_data = command.split()
    action = command_data[0]
    index = int(command_data[1])
    power_value_radius = int(command_data[2])
    if action == "Shoot":
        shoot(target, index, power_value_radius)
    elif action == "Add":
        add(target, index, power_value_radius)
    elif action == "Strike":
        strike(target, index, power_value_radius)
    command = input()
print(*target, sep="|")
