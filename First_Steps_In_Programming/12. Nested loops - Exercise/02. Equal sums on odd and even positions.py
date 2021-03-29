start = int(input())
end = int(input())
for number in range(start, end + 1):
    odd_sum = 0
    even_sum = 0
    number_to_str = str(number)
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end=" ")