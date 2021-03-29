n = int(input())
for square in range(1, n + 1):
    if square == 1:
        print('+' + ' -' * (n - 2) + ' +')
    elif square == n:
        print('+' + ' -' * (n - 2) + ' +')
    else:
        print('|' + ' -' * (n - 2) + ' |')