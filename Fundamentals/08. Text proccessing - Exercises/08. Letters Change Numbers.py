import string

alphabet_upper = list(string.ascii_uppercase)
alphabet_lower = list(string.ascii_lowercase)
given_text = input().split()
total_sum = 0
for element in given_text:
    mid_sum = 0
    number = int(element[1:len(element) - 1])
    first_num = 0
    second_num = 0
    if element[0].isupper():
        first_num += alphabet_upper.index(element[0]) + 1
        mid_sum += number / first_num
    else:
        first_num += alphabet_lower.index(element[0]) + 1
        mid_sum += number * first_num
    if element[-1].isupper():
        second_num += alphabet_upper.index(element[-1]) + 1
        mid_sum -= second_num
    else:
        second_num += alphabet_lower.index(element[-1]) + 1
        mid_sum += second_num
    total_sum += mid_sum
print(f"{total_sum:.2f}")