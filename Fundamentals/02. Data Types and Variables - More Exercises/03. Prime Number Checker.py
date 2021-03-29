given_num = int(input())
number_is_prime = False
if given_num > 1:
    for i in range(2, given_num):
        if (given_num % i) == 0:
            break
        else:
            number_is_prime = True
if number_is_prime:
    print("True")
else:
    print("False")

