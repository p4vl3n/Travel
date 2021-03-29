resource = input()
my_dict = {}
while not resource == "stop":
    quantitiy = int(input())
    if resource not in my_dict:
        my_dict[resource] = quantitiy
    else:
        my_dict[resource] += quantitiy
    resource = input()
for key, value in my_dict.items():
    print(f"{key} -> {value}")