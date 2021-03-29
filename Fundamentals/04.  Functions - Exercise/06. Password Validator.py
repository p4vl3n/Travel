def password_checker(keyword):
    digits_in_keyword = 0
    password_is_valid = True
    for el in keyword:
        if el.isdigit():
            digits_in_keyword += 1
    if len(keyword) < 6 or len(keyword) > 10:
        print(f"Password must be between 6 and 10 characters")
        password_is_valid = False
    if not keyword.isalnum():
        print(f"Password must consist only of letters and digits")
        password_is_valid = False
    if digits_in_keyword < 2:
        print(f"Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        return print(f"Password is valid")


password = input()
password_checker(password)

