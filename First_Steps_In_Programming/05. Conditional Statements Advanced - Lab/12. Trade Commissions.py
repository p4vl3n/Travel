city = input()
sales = float(input())
commission = 0
if city == "Sofia":
    if sales >= 0:
        if 0 <= sales <= 500:
            commission = 0.05 * sales
        elif 500 < sales <= 1000:
            commission = 0.07 * sales
        elif 1000 < sales <= 10000:
            commission = 0.08 * sales
        else:
            commission = 0.12 * sales
        print(f'{commission:.2f}')
    else:
        print('error')
elif city == "Varna":
    if sales >= 0:
        if 0 <= sales <= 500:
            commission = 0.045 * sales
        elif 500 < sales <= 1000:
            commission = 0.075 * sales
        elif 1000 < sales <= 10000:
            commission = 0.10 * sales
        else:
            commission = 0.13 * sales
        print(f'{commission:.2f}')
    else:
        print('error')
elif city == "Plovdiv":
    if sales >= 0:
        if 0 <= sales <= 500:
            commission = 0.055 * sales
        elif 500 < sales <= 1000:
            commission = 0.08 * sales
        elif 1000 < sales <= 10000:
            commission = 0.12 * sales
        else:
            commission = 0.145 * sales
        print(f'{commission:.2f}')
    else:
        print('error')
else:
    print('error')
