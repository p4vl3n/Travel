def it_is_valid(cont_passwrds, given_cont, given_pass):
    for k, v in cont_passwrds.items():
        if k == given_cont and v == given_pass:
            return True
    return False


def student_and_highest_score(cont_students):
    best_student = ""
    best_score = 0
    for stdnt, scr in cont_students.items():
        total_score = 0
        for grade in scr.values():
            total_score += grade
        if total_score > best_score:
            best_student = stdnt
            best_score = total_score
    return best_student, best_score


cont_passwrds = {}
contestants = {}

command = input()
while not command == "end of contests":
    contest, password = command.split(":")
    if contest not in cont_passwrds:
        cont_passwrds[contest] = password
    command = input()

submission = input()
while not submission == "end of submissions":
    contest, password, student, score = submission.split("=>")
    score = int(score)
    if it_is_valid(cont_passwrds, contest, password):
        if student not in contestants:
            contestants[student] = {}
            contestants[student][contest] = score
        if contest not in contestants[student]:
            contestants[student][contest] = score
        else:
            if score > contestants[student][contest]:
                contestants[student][contest] = score
    submission = input()

student, score = student_and_highest_score(contestants)
print(f"Best candidate is {student} with total {score} points.\nRanking:")


sorted_contestants = dict(sorted(contestants.items(), key=lambda x: x[0]))
for k, v in sorted_contestants.items():
    sorted_contestants[k] = dict(sorted(sorted_contestants[k].items(), key=lambda x: -x[1]))

for student, performance in sorted_contestants.items():
    print(f"{student}")
    for contest, score in performance.items():
        print(f"#  {contest} -> {score}")


