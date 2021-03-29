words = input().split(", ")
words_to_match = input().split(", ")
new_list = []
for word in words:
    for el in words_to_match:
        if word in el:
            if word in new_list:
                continue
            else:
                new_list.append(word)
print(new_list)