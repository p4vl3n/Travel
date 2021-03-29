given_text = input()
encrypted = ""
for char in given_text:
    code_num = ord(char) + 3
    new_char = chr(code_num)
    encrypted += new_char
print(encrypted)

