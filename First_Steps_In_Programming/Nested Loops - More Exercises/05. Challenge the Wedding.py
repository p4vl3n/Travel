males = int(input())
females = int(input())
tables = int(input())
for male in range(1, males + 1):
    for female in range(1, females + 1):
        if tables > 0:
            print(f'({male} <-> {female})', end=" ")
            tables -= 1
        else:
            exit(0)