given_string = list(input())
my_dict = {}
for el in given_string:
    if el == " ":
        continue
    if el not in my_dict:
        my_dict[el] = 0
    my_dict[el] += 1
for key in my_dict:
    print(f"{key} -> {my_dict[key]}")
