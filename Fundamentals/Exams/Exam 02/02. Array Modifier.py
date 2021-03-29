given_list = list(map(int, input().split()))
command_data = input()
while not command_data == "end":
    to_do = command_data.split()
    action = to_do[0]
    if action == "swap":
        index_1 = int(to_do[1])
        index_2 = int(to_do[2])
        given_list[index_1], given_list[index_2] = given_list[index_2], given_list[index_1]
    elif action == "multiply":
        index_1 = int(to_do[1])
        index_2 = int(to_do[2])
        new_element = given_list[index_1] * given_list[index_2]
        given_list[index_1] = new_element
    elif action == "decrease":
        given_list = [num - 1 for num in given_list]
    command_data = input()
print(*given_list, sep=", ")