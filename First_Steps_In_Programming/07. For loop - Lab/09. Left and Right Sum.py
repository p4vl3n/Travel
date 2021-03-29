num = int(input())
sum_one = 0
sum_two = 0
for first_sum in range(num):
    first_num = int(input())
    sum_one += first_num
for second_sum in range(num):
    first_num = int(input())
    sum_two += first_num
if sum_one == sum_two:
    print(f'Yes, sum = {sum_one}')
else:
    print(f'No, diff = {abs(sum_one - sum_two)}')