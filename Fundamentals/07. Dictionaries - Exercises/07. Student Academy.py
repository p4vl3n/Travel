rows = int(input())
students = {}
for row in range(rows):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)

for student in students:
    avg_grade = sum(students[student]) / len(students[student])
    students[student] = avg_grade
sorted_students = dict(sorted(students.items(), key=lambda kvp: -kvp[1]))
for student, grade in sorted_students.items():
    if grade >= 4.50:
        print(f"{student} -> {grade:.2f}")