year = 365
days_off = int(input())
working_days = year - days_off
cat_play_limit = 30000
total_play_hours = days_off * 127 + working_days * 63
difference = abs(total_play_hours - cat_play_limit)
hours = difference // 60
minutes = difference % 60
if total_play_hours > cat_play_limit:
    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print("Tom sleeps well")
    print(f'{hours} hours and {minutes} minutes less for play')
