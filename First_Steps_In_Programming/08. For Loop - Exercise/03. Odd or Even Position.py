import sys
numbers = int(input())
odd_sum = 0
odd_max = - sys.maxsize
odd_min = sys.maxsize
even_sum = 0
even_max = - sys.maxsize
even_min = sys.maxsize
for num in range(1, numbers + 1):
    entry_num = float(input())
    if num % 2 == 0:
        even_sum += entry_num
        if entry_num >= even_max:
            even_max = entry_num
        if entry_num <= even_min:
            even_min = entry_num
    else:
        odd_sum += entry_num
        if entry_num >= odd_max:
            odd_max = entry_num
        if entry_num <= odd_min:
            odd_min = entry_num

print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == - sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')
if even_max == - sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
