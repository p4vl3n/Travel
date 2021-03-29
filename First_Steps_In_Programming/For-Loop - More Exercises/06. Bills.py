electricity = 0
water = 0
internet = 0
months = int(input())
for month in range(months):
    water += 20
    internet += 15
    electricity_bill = float(input())
    electricity += electricity_bill
others = 1.20 * (electricity + water + internet)
total_expenses = electricity + water + internet + others
average = total_expenses / months
print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')
