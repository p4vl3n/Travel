items = list(map(int, input().split()))
entry_point = int(input())
item_cost = input()
left_sum = 0
right_sum = 0
for i in range(entry_point):
    if item_cost == "cheap":
        if items[entry_point] > items[i]:
            left_sum += items[i]
    elif item_cost == "expensive":
        if items[entry_point] <= items[i]:
            left_sum += items[i]
for ind in range(entry_point + 1, len(items)):
    if item_cost == "cheap":
        if items[entry_point] > items[ind]:
            right_sum += items[ind]
    elif item_cost == "expensive":
        if items[entry_point] <= items[ind]:
            right_sum += items[ind]
if right_sum > left_sum:
    print(f"Right - {right_sum}")
else:
    print(f"Left - {left_sum}")