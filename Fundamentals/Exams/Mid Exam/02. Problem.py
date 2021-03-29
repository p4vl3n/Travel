friends_list = input().split(", ")
command = input()
while not command == "Report":
    command_data = command.split()
    action = command_data[0]
    if action == "Blacklist":
        name = command_data[1]
        if name in friends_list:
            index = friends_list.index(name)
            friends_list[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif action == "Error":
        index = int(command_data[1])
        if 0 <= index < len(friends_list):
            if not friends_list[index] == "Blacklisted" and not friends_list[index] == "Lost":
                print(f"{friends_list[index]} was lost due to an error.")
                friends_list[index] = "Lost"
    elif action == "Change":
        index = int(command_data[1])
        if 0 <= index < len(friends_list):
            new_name = command_data[2]
            print(f"{friends_list[index]} changed his username to {new_name}.")
            friends_list[index] = new_name
    command = input()
blacklisted = 0
lost = 0
for name in friends_list:
    if name == "Blacklisted":
        blacklisted += 1
    elif name == "Lost":
        lost += 1
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(*friends_list)