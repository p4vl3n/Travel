contestants = {}
student_scores = {}
command = input()
while not command == "no more time":
    student, course, score = command.split(" -> ")
    score = int(score)
    if course not in contestants:
        contestants[course] = {student: score}
        if student not in student_scores:
            student_scores[student] = score
        else:
            student_scores[student] += score

    else:
        if student not in contestants[course]:
            contestants[course][student] = score
            if student not in student_scores:
                student_scores[student] = score
            else:
                student_scores[student] += score
        else:
            if score > contestants[course][student]:
                student_scores[student] += score - contestants[course][student]
                contestants[course][student] = score
                
    command = input()


for contest in contestants:
    contestants[contest] = dict(sorted(contestants[contest].items(), key=lambda x: (-x[1], x[0])))
sorted_students = dict(sorted(student_scores.items(), key=lambda x: (-x[1], x[0])))

for contest, students in contestants.items():
    print(f"{contest}: {len(contestants[contest])} participants")
    count = 1
    for student, score in students.items():
        print(f"{count}. {student} <::> {score}")
        count += 1
count = 1
print(f"Individual standings:")
for student, score in sorted_students.items():
    print(f"{count}. {student} -> {score}")
    count += 1
