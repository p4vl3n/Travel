def shorter_string(first, second):
    if len(first) >= len(second):
        return first, second
    return second, first

given_string = input().split()
first_word = given_string[0]
second_word = given_string[1]
longer, shorter = shorter_string(first_word, second_word)
total_sum = 0
for index in range(len(shorter)):
    mid_sum = ord(longer[index]) * ord(shorter[index])
    total_sum += mid_sum
for ind in range(len(shorter), len(longer)):
    total_sum += ord(longer[ind])
print(total_sum)