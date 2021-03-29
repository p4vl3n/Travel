def factorial_division(x, y):
    sum_to_divide = 1
    dividers = 1
    for num in range(2, x + 1):
        sum_to_divide *= num
    for divider in range(2, y + 1):
        dividers *= divider
    return f"{sum_to_divide/dividers:.2f}"


first_num = int(input())
second_num = int(input())
result = factorial_division(first_num,second_num)
print(result)
