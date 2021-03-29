n = int(input())
for magic_number in range(1111, 10000):
    number_is_magical = True
    string_number = str(magic_number)
    for digit in string_number:
        int_digit = int(digit)
        if int_digit == 0:
            number_is_magical = False
            break
        elif n % int(digit) != 0:
            number_is_magical = False
    if number_is_magical:
        print(magic_number, end=" ")