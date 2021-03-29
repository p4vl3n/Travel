from math import floor
income = float(input())
grade = float(input())
min_wage = float(input())
excellent_scholarship = floor(grade * 25)
social_scholarship = floor(0.35 * min_wage)
if grade >= 5.50:
    print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
elif grade > 4.50:
    if income < min_wage:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")
