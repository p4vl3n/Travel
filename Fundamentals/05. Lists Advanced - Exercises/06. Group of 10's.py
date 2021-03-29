list_as_ints = list(map(int, input().split(", ")))
group = 10
while list_as_ints:
    list_to_print = [num for num in list_as_ints if num <= group]
    for el in list_to_print:
        list_as_ints.remove(el)
    print(f"Group of {group}'s: {list_to_print}")
    group += 10
