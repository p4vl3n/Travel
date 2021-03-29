n = int(input())
a = 0
b = 0
c = 0
d = 0
for number in range(1111, 10000):
    number_as_string = str(number)
    for index, digit in enumerate(number_as_string):
        if index == 0:
            a = int(digit)
        elif index == 1:
            b = int(digit)
        elif index == 2:
            c = int(digit)
        else:
            d = int(digit)
    sum_of_first_two = a + b
    sum_of_second_two = c + d
    if sum_of_first_two == sum_of_second_two and n % sum_of_first_two == 0:
        if a == 0 or b == 0 or c == 0 or d == 0:
            continue
        else:
            print(number, end=" ")