import re

pattern = r"%(?P<name>[A-Z][a-z]+)%[^\$\|%\.]*<(?P<product>[a-zA-Z]+)>[^\$\|%\.]*\|(?P<quantity>\d+)\|([^\$\|%\.0-9]*|(?<=\|))(?P<price>\d+(\.\d+)?)\$"
total_income = 0
text = input()
while not text == "end of shift":
    things = [obj.groupdict() for obj in re.finditer(pattern, text)]
    if things:
        total_order = int(things[0]['quantity']) * float(things[0]['price'])
        total_income += total_order
        print(f"{things[0]['name']}: {things[0]['product']} - {total_order:.2f}")
    text = input()  
print(f"Total income: {total_income:.2f}")

