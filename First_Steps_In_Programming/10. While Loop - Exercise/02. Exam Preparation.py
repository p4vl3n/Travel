allowed_bad_grades = int(input())
count_of_bad_grades = allowed_bad_grades
problem = input()
total_score = 0
problems = 0
need_a_break = False
last_problem = ""
while problem != "Enough":
    score = float(input())
    total_score += score
    problems += 1
    last_problem = problem
    if score <= 4:
        count_of_bad_grades -= 1
        if count_of_bad_grades <= 0:
            need_a_break = True
            break
    problem = input()

average_score = total_score / problems
if need_a_break:
    print(f"You need a break, {allowed_bad_grades} poor grades.")
else:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {problems}')
    print(f'Last problem: {last_problem}')
