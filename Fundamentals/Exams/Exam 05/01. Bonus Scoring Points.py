count_of_students = int(input())
count_of_lectures = int(input())
additional_bonus = int(input())
best_score = 0
best_student_attendances = 0
for student in range(count_of_students):
    attendances = int(input())
    total_bonus = attendances / count_of_lectures * (5 + additional_bonus)
    if total_bonus >= best_score:
        best_score = total_bonus
        best_student_attendances = attendances

print(f"Max Bonus: {round(best_score)}.")
print(f"The student has attended {best_student_attendances} lectures.")