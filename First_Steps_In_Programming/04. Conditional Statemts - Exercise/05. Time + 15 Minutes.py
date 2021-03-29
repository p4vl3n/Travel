hour = int(input())
minutes = int(input())
total_minutes = hour * 60 + minutes
new_total_minutes = total_minutes + 15
new_hour = new_total_minutes // 60
new_minutes = new_total_minutes % 60
if new_hour >= 24:
    new_hour -= 24
if new_minutes < 10:
    print(f'{new_hour}:0{new_minutes}')
else:
    print(f'{new_hour}:{new_minutes}')