given_string = input()
emoticons = []
for index in range(len(given_string)):
    if given_string[index] == ":":
        emoticon = ":" + given_string[index + 1]
        emoticons.append(emoticon)

print("\n".join(emoticons))