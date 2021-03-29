lines = int(input())
key_word = input()

all_given_strings = []
key_word_strings = []

for line in range(lines):
    all_given_strings.append(input())

for i in all_given_strings:
    if key_word in i:
        key_word_strings.append(i)

print(all_given_strings)
print(key_word_strings)
