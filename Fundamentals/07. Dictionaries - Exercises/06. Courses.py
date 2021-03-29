courses = {}
course_participants = {}
input_line = input()
while not input_line == "end":
    course, participant = input_line.split(" : ")
    if course not in courses:
        courses[course] = 1
        course_participants[course] = []
        course_participants[course].append(participant)
    else:
        courses[course] += 1
        course_participants[course].append(participant)
    input_line = input()

sorted_courses = dict(sorted(courses.items(), key=lambda kvp: -kvp[1]))
sorted_participants = {}
for course, participants in course_participants.items():
    sorted_participants[course] = sorted(course_participants[course])


for course, occurances in sorted_courses.items():
    print(f"{course}: {occurances}")
    for school, participants in sorted_participants.items():
        if course == school:
            for participant in participants:
                print(f"-- {participant}")

