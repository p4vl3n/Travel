shopping_list = input().split("!")
command_data = input()
while not command_data == "Go Shopping!":
    actions = command_data.split()
    importance = actions[0]
    item = actions[1]
    if len(actions) == 3:
        new_item = actions[2]
    if importance == "Urgent":
        if item in shopping_list:
            pass
        else:
            shopping_list.insert(0, item)
    elif importance == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            pass
    elif importance == "Correct":
        if item in shopping_list:
            for i, n in enumerate(shopping_list):
                if n == item:
                    shopping_list[i] = new_item
        else:
            pass
    elif importance == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
        else:
            pass
    command_data = input()
print(", ".join(shopping_list))