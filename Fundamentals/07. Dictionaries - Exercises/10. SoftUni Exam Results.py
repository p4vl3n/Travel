from collections import defaultdict
courses = defaultdict(int)
students = {}
command = input()
while not command == "exam finished":
    command_data = command.split("-")
    if len(command_data) == 3:
        student, course, score = command.split("-")
        courses[course] += 1
        if student not in students:
            students[student] = int(score)
        else:
            if students[student] < int(score):
                students[student] = int(score)
    else: 
        student, banned = command.split("-")
        students.pop(student)
    command = input()
sorted_courses = dict(sorted(courses.items(), key=lambda kvp: (-kvp[1], kvp[0])))
sorted_students = dict(sorted(students.items(), key=lambda kvp: (-kvp[1], kvp[0])))
print("Results:")
for student, score in sorted_students.items():
    print(f"{student} | {score}")
print("Submissions:")
for course, submission in sorted_courses.items():
    print(f"{course} - {submission}")

