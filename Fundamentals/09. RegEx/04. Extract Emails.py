import re


given_text = input()
pattern = r"(^|\s)[a-zA-Z]+[\.\-]?[a-zA-Z]+@[a-zA-Z]+(\-[a-zA-Z]+)?(\.[a-zA-Z]+)+"
mail = [obj.group() for obj in re.finditer(pattern, given_text)]
print(*mail, sep="\n")