given_list = input().split()
given_string = list(input())
new_list = []
encrypted_message = ""
for el in given_list:
    small_list = []
    for digit in el:
        small_list.append(digit)
    small_list = list(map(int, small_list))
    new_list.append(small_list)
for number in new_list:
    if sum(number) > len(given_string):
        index = sum(number) - len(given_string)
        letter = given_string[index]
        encrypted_message += letter
        given_string.pop(index)
    else:
        letter = given_string[sum(number)]
        encrypted_message += letter
        given_string.pop(sum(number))

print(encrypted_message)


