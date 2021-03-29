given_list = list(map(int, input().split()))
average = sum(given_list) / len(given_list)
top_nums = [num for num in given_list if num > average]
if len(top_nums) >= 5:
    top_nums.sort(reverse=True)
    print(*top_nums[:5:])
elif len(top_nums) >= 1:
    top_nums.sort(reverse=True)
    print(*top_nums)
else:
    print("No")