import sys
pairs = int(input())
previous_pair = 0
next_pair = 0
max_diff = - sys.maxsize
difference = 0
value = 0
pairs_have_same_values = True
for pair in range(pairs):
    number_one = int(input())
    number_two = int(input())
    if pair == 0:
        previous_pair = number_one + number_two
        value = number_one + number_two
    else:
        next_pair = number_one + number_two
        if previous_pair != next_pair:
            difference = abs(previous_pair - next_pair)
            if difference >= max_diff:
                max_diff = difference
            pairs_have_same_values = False
        else:
            value = number_one + number_two
        previous_pair = next_pair
if pairs_have_same_values:
    print(f'Yes, value={value}')
else:
    print(f'No, maxdiff={max_diff}')