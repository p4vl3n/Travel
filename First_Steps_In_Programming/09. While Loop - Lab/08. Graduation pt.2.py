student = input()
score = 0
grade = 0
passed = True
total_score = 0
while grade < 12:
    grade += 1
    score = float(input())
    if score < 4:
        score = float(input())
        if score < 4:
            passed = False
            break
        total_score += score
    else:
        total_score += score
average_score = total_score / grade
if not passed:
    print(f'{student} has been excluded at {grade} grade')
else:
    print(f'{student} graduated. Average grade: {average_score:.2f}')

