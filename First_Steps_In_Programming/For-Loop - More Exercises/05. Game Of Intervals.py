turns = int(input())
score = 0
low_range = 0
mid_low_range = 0
mid_range = 0
mid_high_range = 0
high_range = 0
invalid_nums = 0
for turn in range(turns):
    num = int(input())
    if 0 <= num < 10:
        low_range += 1
        score += 0.20 * num
    elif 10 <= num < 20:
        mid_low_range += 1
        score += 0.30 * num
    elif 20 <= num < 30:
        mid_range += 1
        score += 0.40 * num
    elif 30 <= num < 40:
        mid_high_range += 1
        score += 50
    elif 40 <= num <= 50:
        high_range += 1
        score += 100
    else:
        invalid_nums += 1
        score *= 0.50
total_nums = low_range + mid_low_range + mid_range + mid_high_range + high_range + invalid_nums
print(f'{score:.2f}')
print(f'From 0 to 9: {low_range / total_nums * 100:.2f}%')
print(f'From 10 to 19: {mid_low_range / total_nums * 100:.2f}%')
print(f'From 20 to 29: {mid_range / total_nums * 100:.2f}%')
print(f'From 30 to 39: {mid_high_range / total_nums * 100:.2f}%')
print(f'From 40 to 50: {high_range / total_nums * 100:.2f}%')
print(f'Invalid numbers: {invalid_nums / total_nums * 100:.2f}%')
