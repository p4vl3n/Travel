height = int(input())
target_is_achieved = False
jumps = 0
jump_height = 0
target = height - 30
while target <= height:
    for attempt in range(3):
        target_is_achieved = False
        jump_height = int(input())
        jumps += 1
        if jump_height > target:
            target_is_achieved = True
            break
    target += 5
    if not target_is_achieved:
        break
if target_is_achieved:
    print(f"Tihomir succeeded, he jumped over {height}cm after {jumps} jumps.")
else:
    print(f"Tihomir failed at {jump_height}cm after {jumps} jumps.")
