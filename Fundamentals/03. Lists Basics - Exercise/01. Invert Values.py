given_list = input().split(" ")
new_list = []
for element in given_list:
    new_element = int(element)
    new_list.append(new_element * (- 1))
print(new_list)