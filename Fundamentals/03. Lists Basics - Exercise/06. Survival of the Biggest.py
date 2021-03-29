from sys import maxsize
given_list = input().split(" ")
removals = int(input())
smallest_num = maxsize
for removal in range(removals):
    for element in given_list:
        if int(element) < smallest_num:
            smallest_num = int(element)
    for element in given_list:
        if int(element) == smallest_num:
            given_list.remove(element)
    smallest_num = maxsize
for i in range(len(given_list)):
    given_list[i] = int(given_list[i])
print(given_list)