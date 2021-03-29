first_string = input()
second_string = input()
new_string = ""
previous_string = first_string
for index in range(len(first_string)):
    for i in range(index + 1):
        new_string += second_string[i]
    for i in range(index + 1, len(second_string)):
        new_string += first_string[i]
    if not new_string == previous_string:
        print(new_string)
    previous_string = new_string
    new_string = ""