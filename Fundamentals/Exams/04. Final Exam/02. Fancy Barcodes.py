import re

n = int(input())
pattern = r"(@#+)(?P<bar_code>[A-Z][A-Za-z0-9]{4,}[A-Z])\1"
dig = r"\d"
for _ in range(n):
    text = input()
    match = [obj for obj in re.finditer(pattern, text)]
    if match:
        for m in match:
            digits = re.findall(dig, m.group('bar_code'))
            if digits:
                print(f"Product group: {''.join(digits)}")
            else:
                print(f"Product group: 00")
    else:
        print(f"Invalid barcode")
