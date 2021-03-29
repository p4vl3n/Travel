count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for numbers in range(count):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1
print(f'{p1 / count * 100:.2f}%')
print(f'{p2 / count * 100:.2f}%')
print(f'{p3 / count * 100:.2f}%')
print(f'{p4 / count * 100:.2f}%')
print(f'{p5 / count * 100:.2f}%')