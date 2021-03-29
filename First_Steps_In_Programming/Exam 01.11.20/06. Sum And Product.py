n = int(input())
combination_is_found = False
for a in range(1, 10):
    for b in range(9, a - 1, - 1):
        for c in range(0,10):
            for d in range(9, c - 1, - 1):
                if n % 10 == 5:
                    if (a + b + c + d) == (a * b * c * d):
                        print(f'{a}{b}{c}{d}')
                        combination_is_found = True
                        break
                elif n % 3 == 0:
                    if (a * b * c * d) // (a + b + c + d) == 3:
                        print(f'{d}{c}{b}{a}')
                        combination_is_found = True
                        break
            if combination_is_found:
                break
        if combination_is_found:
            break
    if combination_is_found:
        break
if not combination_is_found:
    print("Nothing found")