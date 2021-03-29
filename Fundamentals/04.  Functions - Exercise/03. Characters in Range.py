def chars_in_range(a, b):
    characters_in_range = []
    for i in range(ord(a) + 1, ord(b)):
        char = chr(i)
        characters_in_range.append(char)
    return " ".join(characters_in_range)


first_char = input()
second_char = input()
result = chars_in_range(first_char, second_char)
print(result)