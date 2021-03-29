activation_key = input()
command = input()
while not command == "Generate":
    data = command.split(">>>")
    action = data[0]
    if action == "Contains":
        substring = data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif action == "Flip":
        upper_lower, start_index, end_index = data[1], int(data[2]), int(data[3])
        if upper_lower == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
            print(activation_key)
        elif upper_lower == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
            print(activation_key) 
    elif action == "Slice":
            start_index, end_index = int(data[1]), int(data[2])
            activation_key = activation_key[:start_index] + activation_key[end_index:]
            print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")