given_string = input()
new_string = "" 
index = 0
while index < len(given_string) - 1:
    if given_string[index] == given_string[index + 1]:
        element_to_replace = f"{given_string[index]}{given_string[index + 1]}"
        given_string = given_string.replace(element_to_replace, given_string[index])
        if not index:
            continue
        else:
            index -= 1
    else:
        index += 1
print(given_string)
