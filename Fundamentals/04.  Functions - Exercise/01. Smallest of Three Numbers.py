from sys import maxsize


def smallest_of_three(list_of_nums):
    smallest = maxsize
    for num in list_of_nums:
        if int(num) <= smallest:
            smallest = num
    return smallest


given_num1 = int(input())
given_num2 = int(input())
given_num3 = int(input())
given_ints = [given_num1, given_num2, given_num3]

result = smallest_of_three(given_ints)
print(result)
