vip = 499.99
regular = 249.99
budget = float(input())
category = input()
fans = int(input())
vip_price = vip * fans
regular_price = regular * fans
transport = 0
if 1 <= fans <= 4:
    transport = 0.75 * budget
elif 5 <= fans <=9:
    transport = 0.60 * budget
elif 10 <= fans <= 24:
    transport = 0.50 * budget
elif 25 <= fans <= 49:
    transport = 0.40 * budget
elif fans >= 50:
    transport = 0.25 * budget
ticket_budget = budget - transport
vip_difference = abs(ticket_budget - vip_price)
regular_difference = abs(ticket_budget - regular_price)
if category == "VIP":
    if ticket_budget >= vip_price:
        print(f'Yes! You have {vip_difference:.2f} leva left.')
    else:
        print(f'Not enough money! You need {vip_difference:.2f} leva.')
elif category == "Normal":
    if ticket_budget >= regular_price:
        print(f'Yes! You have {regular_difference:.2f} leva left.')
    else:
        print(f'Not enough money! You need {regular_difference:.2f} leva.')


