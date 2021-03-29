exam_starting_hour = int(input())
exam_starting_minutes = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
exam_start = exam_starting_hour * 60 + exam_starting_minutes
arrival = hour_of_arrival * 60 + minute_of_arrival
difference = abs(exam_start - arrival)
hour = difference // 60
minute = difference % 60
if arrival <= exam_start - 60:
    print('Early')
    if minute < 10:
        print(f'{hour}:0{minute} hours before the start')
    else:
        print(f'{hour}:{minute} hours before the start')
elif exam_start - 60 < arrival < exam_start - 30:
    print('Early')
    print(f'{minute} minutes before the start')
elif exam_start - 30 <= arrival <= exam_start:
    print('On time')
    print(f'{minute} minutes before the start')
elif exam_start + 60 > arrival > exam_start:
    print('Late')
    print(f'{minute} minutes after the start')
elif arrival >= exam_start + 60:
    print('Late')
    if minute < 10:
        print(f'{hour}:0{minute} hours after the start')
    else:
        print(f'{hour}:{minute} hours after the start')