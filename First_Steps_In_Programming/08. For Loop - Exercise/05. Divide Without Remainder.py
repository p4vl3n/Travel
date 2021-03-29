count = int(input())
div_by_2 = 0
div_by_3 = 0
div_by_4 = 0
for numbers in range(count):
    number = int(input())
    if number % 2 == 0:
        div_by_2 += 1
    if number % 3 == 0:
        div_by_3 += 1
    if number % 4 == 0:
        div_by_4 += 1
print(f'{div_by_2 / count * 100:.2f}%')
print(f'{div_by_3 / count * 100:.2f}%')
print(f'{div_by_4 / count * 100:.2f}%')