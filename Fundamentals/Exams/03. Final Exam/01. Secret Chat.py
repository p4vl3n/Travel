given_string = input()
command = input()
while not command == "Reveal":
    data = command.split(":|:")
    action = data[0]
    if action == "InsertSpace":
        index = int(data[1])
        if 0 <= index < len(given_string):
            given_string = given_string[:index] + " " + given_string[index:]
            print(given_string)
    elif action == "Reverse":
        reversed_sub_str = data[1]
        sub_str = reversed_sub_str[::-1]
        if reversed_sub_str in given_string:
            given_string = given_string.replace(reversed_sub_str, "", 1)
            given_string = given_string + sub_str
            print(given_string)
        else:
            print(f"error")
    elif action == "ChangeAll":
        to_replace = data[1]
        new_letter = data[2]
        if to_replace in given_string:
            given_string = given_string.replace(to_replace, new_letter)
        print(given_string)
    command = input()
print(f"You have a new text message: {given_string}")