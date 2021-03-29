entry = input()
working_day = "Working day"
day_off = "Weekend"
if entry == "Monday" or entry == "Tuesday" or entry == "Wednesday" or entry == "Thursday" or entry == "Friday":
    print(working_day)
elif entry == "Saturday" or entry == "Sunday":
    print(day_off)
else:
    print('Error')