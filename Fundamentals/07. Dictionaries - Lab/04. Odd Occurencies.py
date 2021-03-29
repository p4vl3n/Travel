words = input().split()
dictionary = {}
for word in words:
    l_case_word = word.lower()
    if l_case_word not in dictionary:
        dictionary[l_case_word] = 0
    dictionary[l_case_word] += 1

for key, value in dictionary.items():
    if not value % 2 == 0:
        print(f"{key}", end=" ")