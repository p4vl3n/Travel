n = int(input())
printed_number = 1
number_equals_n = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if printed_number > n:
            number_equals_n = True
            break
        print(f'{printed_number}', end=" ")
        printed_number += 1
    if number_equals_n:
        break
    print()