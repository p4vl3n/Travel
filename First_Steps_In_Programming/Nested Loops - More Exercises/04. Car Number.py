start = int(input())
end = int(input())
for first_digit in range(start, end + 1):
    for second_digit in range(start, end + 1):
        for third_digit in range(start, end + 1):
            for fourth_digit in range(start, end + 1):
                sum_of_second_and_third = second_digit + third_digit
                if first_digit % 2 == 0 and fourth_digit % 2 != 0 and first_digit > fourth_digit and sum_of_second_and_third % 2 == 0:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=" ")
                elif first_digit % 2 != 0 and fourth_digit % 2 == 0 and first_digit > fourth_digit and sum_of_second_and_third % 2 == 0:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=" ")