balance = 0
command = input()
while command != "NoMoreMoney":
    increase = float(command)
    if increase < 0:
        print('Invalid operation!')
        break
    balance += increase
    print(f'Increase: {increase:.2f}')
    command = input()
print(f'Total: {balance:.2f}')