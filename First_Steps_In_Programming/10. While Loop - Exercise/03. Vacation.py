vacation_cost = float(input())
current_budget = float(input())
total_days = 0
spending_days = 0
jessy_is_a_big_spender = False
while current_budget < vacation_cost:
    action = input()
    amount = float(input())
    total_days += 1
    if action == "spend":
        spending_days += 1
        current_budget -= amount
        if current_budget < 0:
            current_budget = 0
        if spending_days == 5:
            jessy_is_a_big_spender = True
            break
    elif action == "save":
        current_budget += amount
        spending_days = 0
if jessy_is_a_big_spender:
    print(f"You can't save the money.")
    print(total_days)
else:
    print(f'You saved the money for {total_days} days.')