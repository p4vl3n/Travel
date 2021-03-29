def sum_of_odd_and_even(number):
    even_sum = 0
    odd_sum = 0
    for el in number:
        if int(el) % 2 == 0:
            even_sum += int(el)
        else:
            odd_sum += int(el)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


given_number = input()
result = sum_of_odd_and_even(given_number)
print(result)