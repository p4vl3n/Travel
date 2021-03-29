given_string = input()
to_decipher = []
digits = []
steps = []
takes = []

for char in given_string:
    if char.isnumeric():
        digits.append(char)
    else:
        to_decipher.append(char)

for i in range(len(digits)):
    if i % 2 == 0:
        steps.append(digits[i])
    else:
        takes.append(digits[i])

steps = [int(x) for x in steps]
takes = [int(x) for x in takes]
index = 0
takings = 0
for step in steps:
    index += step
    for removals in range(takes[takings]):
        if index >= len(to_decipher):
            break
        to_decipher.pop(index)
    takings += 1
print(''.join(to_decipher))