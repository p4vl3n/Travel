contract_duration = input()
contract_type = input()
added_mobile_data = input()
months_to_pay = int(input())
if contract_duration == "one":
    if contract_type == "Small":
        monthly_tax = 9.98
    elif contract_type == "Medium":
        monthly_tax = 18.99
    elif contract_type == "Large":
        monthly_tax = 25.98
    elif contract_type == "ExtraLarge":
        monthly_tax = 35.99
elif contract_duration == "two":
    if contract_type == "Small":
        monthly_tax = 8.58
    elif contract_type == "Medium":
        monthly_tax = 17.09
    elif contract_type == "Large":
        monthly_tax = 23.59
    elif contract_type == "ExtraLarge":
        monthly_tax = 31.79
if added_mobile_data == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    else:
        monthly_tax += 3.85
owed_money = monthly_tax * months_to_pay
if contract_duration == "two":
    owed_money *= 0.9625
print(f'{owed_money:.2f} lv.')