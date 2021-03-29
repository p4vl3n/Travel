def add_and_subtract(x, y, z):
    def addition_of_two(a, b):
        score = a + b
        return score

    def sum_of_first_minus_sum_of_last(c, d):
        score = c - d
        return score
    sum_of_first = addition_of_two(x, y)
    end_result = sum_of_first_minus_sum_of_last(sum_of_first, z)
    return end_result


number_one = int(input())
number_two = int(input())
number_three = int(input())
result = add_and_subtract(number_one, number_two, number_three)
print(result)