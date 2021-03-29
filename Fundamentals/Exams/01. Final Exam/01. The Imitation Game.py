given_string = input()
command = input()
while not command ==  "Decode":
    data = command.split("|")
    action = data[0]
    if action == "Move":
        index = int(data[1])
        changed_string = given_string[index:] + given_string[:index]
        given_string = changed_string
    elif action == "Insert":
        index = int(data[1])
        letter = data[2]
        changed_string = given_string[:index] + letter + given_string[index:]
        given_string = changed_string
    elif action == "ChangeAll":
        to_replace = data[1]
        new_letter = data[2]
        given_string = given_string.replace(to_replace, new_letter)
    command = input()
print(f"The decrypted message is: {given_string}")