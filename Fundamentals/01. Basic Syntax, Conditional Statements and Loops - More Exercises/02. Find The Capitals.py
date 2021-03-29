given_string = input()
required_list = []
for i in range(0, len(given_string)):
    if given_string[i].isupper():
        required_list.append(i)
print(required_list)