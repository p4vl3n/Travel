given_string = input()
new_index = 0
final_message = ""
for i in range(len(given_string)):
    message_to_add = ""
    if given_string[i].isnumeric():
        message_to_add = given_string[new_index:i]
        final_message += message_to_add * int(given_string[i])
        new_index = i + 1
final_message = final_message.upper()
working_list = list(final_message)
working_list = set(working_list)
print(f"Unique symbols used: {len(working_list)}")
print(final_message)