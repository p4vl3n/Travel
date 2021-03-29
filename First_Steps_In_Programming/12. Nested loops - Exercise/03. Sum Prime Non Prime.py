command = ""
prime_sum = 0
non_prime_sum = 0
while True:
    number_is_prime = True
    command = input()
    if command == "stop":
        break
    number = int(command)
    if number < 0:
        print('Number is negative.')
        continue
    for check in range(2, number):
        if number % check == 0:
            non_prime_sum += number
            number_is_prime = False
            break
    if number_is_prime:
        prime_sum += number
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
