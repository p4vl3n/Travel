first_digit_range = int(input())
second_digit_range = int(input())
third_digit_range = int(input())
second_digit_is_prime = False
for digit_first in range(1, first_digit_range + 1):
    if digit_first % 2 == 0:
        if second_digit_range < 7:
            for digit_second in range(2, second_digit_range + 1):
                if digit_second == 2:
                    second_digit_is_prime = True
                for prime in range(2, digit_second):
                    if (digit_second % prime) == 0:
                        break
                    else:
                        second_digit_is_prime = True
                if second_digit_is_prime:
                    second_digit_is_prime = False
                    for digit_third in range(1, third_digit_range + 1):
                        if digit_third % 2 == 0:
                            print(digit_first, digit_second, digit_third)
        else:
            for digit_second in range(2, 7):
                if digit_second == 2:
                    second_digit_is_prime = True
                for prime in range(2, digit_second):
                    if (digit_second % prime) == 0:
                        break
                    else:
                        second_digit_is_prime = True
                if second_digit_is_prime:
                    second_digit_is_prime = False
                    for digit_third in range(1, third_digit_range + 1):
                        if digit_third % 2 == 0:
                            print(digit_first, digit_second, digit_third)