def perfect_number(x):
    positive_divisors = []
    for n in range(1, int(x/2 + 1)):
        if x % n == 0:
            positive_divisors.append(n)
    if sum(positive_divisors) == x:
        return print(f"We have a perfect number!")
    return print(f"It's not so perfect.")


given_number = int(input())
perfect_number(given_number)