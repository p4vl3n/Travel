import re

pattern = r"\d+"
captured_nums = []
text = input()

while not text == "":
    num = re.findall(pattern, text)
    captured_nums.extend(num)
    text = input()
print(*captured_nums)   