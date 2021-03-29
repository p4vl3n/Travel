import sys
number = int(input())
max_num = - sys.maxsize
sum = 0
for num in range(number):
    new_number = int(input())
    sum += new_number
    if new_number > max_num:
        max_num = new_number
if max_num == sum - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - (sum - ma x_num))}')