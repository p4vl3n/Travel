jury = int(input())
presentation_name = input()
exam_average = 0
presentations = 0
while presentation_name != "Finish":
    presentations += 1
    presentation_average = 0
    for presentation in range(jury):
        grade = float(input())
        presentation_average += grade
    presentation_average /= jury
    exam_average += presentation_average
    print(f'{presentation_name} - {presentation_average:.2f}.')
    presentation_name = input()
exam_average /= presentations
print(f"Student's final assessment is {exam_average:.2f}.")