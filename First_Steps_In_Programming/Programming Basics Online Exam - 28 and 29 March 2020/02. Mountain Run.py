world_record = float(input())
distance = float(input())
time_per_meter = float(input())
delay = (distance // 50) * 30
personal_record = distance * time_per_meter + delay
difference = personal_record - world_record
if personal_record < world_record:
    print(f'Yes! The new record is {personal_record:.2f} seconds.')
else:
    print(f'No! He was {difference:.2f} seconds slower.')
