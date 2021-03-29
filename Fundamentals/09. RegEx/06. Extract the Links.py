import re


text = input()
pattern = r"(w{3}\.)([a-zA-Z0-9-]+)(\.[a-z]+)+"
websites = []
while text:
    match = [obj.group() for obj in re.finditer(pattern, text)]
    websites.extend(match)
    text = input()
print(*websites, sep="\n")