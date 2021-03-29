n = int(input())
my_dict = {}
for line in range(n):
    key_word = input()
    synonym = input()
    if key_word not in my_dict:
        my_dict[key_word] = []
    my_dict[key_word].append(synonym)
for key, value in my_dict.items():
    print(f"{key} - {', '.join(value)}")


