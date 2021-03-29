a = int(input())
b = int(input())
max_passwords = int(input())
reached_max_password = False
passwords = 0
for a_symbol in range(35, 55):
    for b_symbol in range(64, 96):
        for x_symbol in range(1, a + 1):
            for y_symbol in range(1, b + 1):
                passwords += 1
                if passwords > max_passwords:
                    reached_max_password = True
                    break
                else:
                    print(f"{chr(a_symbol)}{chr(b_symbol)}{x_symbol}{y_symbol}{chr(b_symbol)}{chr(a_symbol)}", end="|")