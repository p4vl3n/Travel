import re


def define_threshold(thr):
    result = 0
    for i in range(len(thr)):
        if not i:
            result = thr[i]
        else:
            result *= thr[i]
    return result

given_string = input()
emoji_patern = r"(?P<emoji>(:{2}|\*{2})(?P<name>[A-Z][a-z]{2,})\2)"
coolnes_pattern = r"\d"
emojis = [emoji.group() for emoji in re.finditer(emoji_patern, given_string)]
threshold_digits = [int(digit) for digit in re.findall(coolnes_pattern, given_string)]
threshold = define_threshold(threshold_digits)
    
cool_emojis = []
for name in emojis:
    name_threshold = 0
    for el in name[2:len(name) - 2]:
        name_threshold += ord(el)
    if name_threshold >= threshold:
        cool_emojis.append(name)
print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
