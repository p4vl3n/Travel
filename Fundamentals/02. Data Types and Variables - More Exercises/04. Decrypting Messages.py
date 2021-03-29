given_key = int(input())
letters = int(input())
message = ""
for i in range(letters):
    given_letter = input()
    decipher = ord(given_letter) + given_key
    new_letter = chr(decipher)
    message += new_letter
print(message)
