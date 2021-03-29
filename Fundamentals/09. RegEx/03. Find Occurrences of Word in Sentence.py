import re

input_string = input()
word = input()
pattern = rf"\b{word}\b"
count = re.findall(pattern, input_string, re.IGNORECASE)
print(len(count))