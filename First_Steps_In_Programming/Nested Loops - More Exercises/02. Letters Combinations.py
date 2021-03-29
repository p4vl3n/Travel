first_letter = input()
second_letter = input()
missing_letter = input()
start_of_interval = ord(first_letter)
end_of_interval = ord(second_letter)
letter_to_miss = ord(missing_letter)
possible_combinations = 0
for letter_one in range(start_of_interval, end_of_interval + 1):
    for letter_two in range(start_of_interval, end_of_interval + 1):
        for letter_three in range(start_of_interval, end_of_interval + 1):
            if letter_one == letter_to_miss or letter_two == letter_to_miss or letter_three == letter_to_miss:
                continue
            else:
                print(f"{chr(letter_one)}{chr(letter_two)}{chr(letter_three)}", end=" ")
                possible_combinations += 1
print(possible_combinations)