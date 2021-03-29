from math import floor
needed_hours = int(input())
free_days = int(input())
workers_on_overtime = int(input())
working_hours = floor((free_days - 0.10 * free_days) * 8)
overtime_hours = free_days * workers_on_overtime * 2
total_working_hours = working_hours + overtime_hours
hours_left = abs(total_working_hours - needed_hours)
if needed_hours <= total_working_hours:
    print(f'Yes!{hours_left} hours left.')
else:
    print(f'Not enough time!{hours_left} hours needed.')