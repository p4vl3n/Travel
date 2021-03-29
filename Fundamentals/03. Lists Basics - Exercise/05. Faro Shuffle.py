given_list = input().split(" ")
shuffles = int(input())
half_list_len = int(len(given_list) / 2)
left_stack = given_list[0:half_list_len]
right_stack = given_list[half_list_len:len(given_list)]
shuffled_deck = []
for shuffle in range(shuffles):
    for i in range(half_list_len):
        shuffled_deck.append(left_stack[i])
        shuffled_deck.append(right_stack[i])
    left_stack = shuffled_deck[0:half_list_len]
    right_stack = shuffled_deck[half_list_len:len(given_list)]
    if shuffle == shuffles - 1:
        continue
    else:
        shuffled_deck = []
print(shuffled_deck)