guest_count = int(input())
entry_fee = float(input())
budget = float(input())
discount = 1
cake = 0.10 * budget
if 10 <= guest_count <= 15:
    discount = 0.85
elif 15 < guest_count <= 20:
    discount = 0.80
elif guest_count > 20:
    discount = 0.75
entry_cost = guest_count * discount * entry_fee
total_cost = entry_cost + cake
diff = abs(total_cost - budget)
if budget >= total_cost:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')