import sys
num = int(input())
max = -sys.maxsize
min = sys.maxsize
for x in range(0, num):
    entry = int(input())
    if entry > max:
        max = entry
    if entry < min:
        min = entry
print(f'Max number: {max}')
print(f'Min number: {min}')
