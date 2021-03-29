secret = input().split()
deciphered = []
for element in secret:
    char = ""
    word = ""
    for el in element:
        if el.isdigit():
            char += el
        else:
            word += el
    secret_word = list(chr(int(char)) + word)
    secret_word[1], secret_word[-1] = secret_word[-1], secret_word[1]
    secret_word = "".join(secret_word)
    deciphered.append(secret_word)
print(*deciphered, sep=" ")

