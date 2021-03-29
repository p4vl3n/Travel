control_number = int(input())
a = 0
b = 0
c = 0
d = 0
password_rotation = 0
password_name = ""
enough_rotations = False
for password in range(1111, 9999):
    string_password = str(password)
    for index, digit in enumerate(string_password):
        if index <= 1:
            if index == 0:
                a = int(digit)
            else:
                b = int(digit)
        else:
            if index == 2:
                c = int(digit)
            else:
                d = int(digit)
    if a < b and c > d:
        if (a*b) + (c*d) == control_number:
            password_rotation += 1
            print(f"{a}{b}{c}{d}", end=" ")
            if password_rotation == 4:
                enough_rotations = True
                password_name = str(a) + str(b) + str(c) + str(d)
print()
if not enough_rotations:
    print('No!')
else:
    print(f'Password: {password_name}')
