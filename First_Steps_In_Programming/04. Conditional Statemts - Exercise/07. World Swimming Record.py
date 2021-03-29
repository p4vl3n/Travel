record = float(input())
distance = float(input())
time_per_meter = float(input())
friction = (distance // 15) * 12.5
time = distance * time_per_meter + friction
difference = abs(record - time)
if time < record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')