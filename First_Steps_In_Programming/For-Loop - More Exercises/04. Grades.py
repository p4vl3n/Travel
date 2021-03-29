students = int(input())
top_students = 0
above_avg = 0
below_avg = 0
fail = 0
grades = 0
for student in range(students):
    grade = float(input())
    grades += grade
    if 2 <= grade < 3:
        fail += 1
    elif 3 <= grade < 4:
        below_avg += 1
    elif 4 <= grade < 5:
        above_avg += 1
    else:
        top_students += 1
avg_grade = grades / students
print(f'Top students: {top_students / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {above_avg / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {below_avg / students * 100:.2f}%')
print(f'Fail: {fail / students * 100:.2f}%')
print(f'Average: {avg_grade:.2f}')
