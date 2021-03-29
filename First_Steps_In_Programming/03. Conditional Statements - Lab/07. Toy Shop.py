puzzle = 2.6
puppet = 3
teddy = 4.1
minion = 8.2
truck = 2
vacation = float(input())
puzzle_order = int(input())
puppet_order = int(input())
teddy_order = int(input())
minion_order = int(input())
truck_order = int(input())
puzzle_cost = puzzle * puzzle_order
puppet_cost = puppet * puppet_order
teddy_cost = teddy * teddy_order
minion_cost = minion * minion_order
truck_cost = truck * truck_order
total_order = puzzle_order + puppet_order + teddy_order + minion_order + truck_order
order_cost = puzzle_cost + puppet_cost + teddy_cost + minion_cost + truck_cost
discounted_cost = 0.75 * order_cost
if total_order >= 50:
    rent = 0.10 * discounted_cost
    earned = discounted_cost - rent
    if earned >= vacation:
        money_left = earned - vacation
        print(f'Yes! {money_left:.2f} lv left.')
    else:
        money_left = vacation - earned
        print(f'Not enough money! {money_left:.2f} lv needed.')
else:
    rent = 0.10 * order_cost
    earned = order_cost - rent
    if earned >= vacation:
        money_left = earned - vacation
        print(f'Yes! {money_left:.2f} lv left.')
    else:
        money_left = vacation - earned
        print(f'Not enough money! {money_left:.2f} lv needed.')