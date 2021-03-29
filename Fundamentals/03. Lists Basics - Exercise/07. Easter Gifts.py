planned_gifts = input().split(" ")
command = input()
while not command == "No Money":
    command_list = command.split(" ")
    if command_list[0] == "OutOfStock":
        for i, e in enumerate(planned_gifts):
            if e == command_list[1]:
                planned_gifts[i] = "None"
    elif command_list[0] == "Required":
        index = int(command_list[2])
        if 0 < index < len(planned_gifts):
            planned_gifts[index] = command_list[1]
    elif command_list[0] == "JustInCase":
        planned_gifts[-1] = command_list[1]
    command = input()
final_list = []
for element in planned_gifts:
    if not element == "None":
        final_list.append(element)
print(" ".join(final_list))




