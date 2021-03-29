given_list = input().split(", ")
for element in given_list:
    if element == "0":
        given_list.remove(element)
        given_list.append("0")
for i, event in enumerate(given_list):
    given_list[i] = int(given_list[i])
print(given_list)
