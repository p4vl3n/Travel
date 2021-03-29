start = int(input())
end = int(input())
magical_number = int(input())
combination_count = 0
found = False
for first_number in range (start, end + 1):
    for second_number in range(start, end + 1):
        combination_count += 1
        if first_number + second_number == magical_number:
            found = True
            print(f'Combination N:{combination_count} ({first_number} + {second_number} = {magical_number})')
            break
    if found:
        break
if not found:
    print(f"{combination_count} combinations - neither equals {magical_number}")