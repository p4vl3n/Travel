num = int(input())
sum_1 = 0
sum_2 = 0
for n in range(1, num + 1):
    num_1 = int(input())
    if n % 2 == 0:
        sum_2 += num_1
    else:
        sum_1 += num_1
if sum_1 == sum_2:
    print('Yes')
    print(f'Sum = {sum_1}')
else:
    print('No')
    print(f'Diff = {abs(sum_1 - sum_2)}')