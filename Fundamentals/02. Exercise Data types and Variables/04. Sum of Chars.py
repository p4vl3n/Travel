num_of_chars = int(input())
sum_of_chars = 0
for char in range(num_of_chars):
    requested_char = input()
    sum_of_chars += ord(requested_char)
print(f"The sum equals: {sum_of_chars}")