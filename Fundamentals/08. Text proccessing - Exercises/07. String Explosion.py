data = input()
given_string = list(data)
new_list = []
index = 0
explosion = 0
for element in given_string:
    if explosion:
        if element == ">":
            new_list.append(element)
        elif element.isdigit():
            explosion += int(element)
            explosion -= 1
        else:
            explosion -= 1
    else:        
        if element.isdigit():
            explosion += int(element)
            explosion -= 1
        else:
            new_list.append(element)
print(*new_list, sep="")



