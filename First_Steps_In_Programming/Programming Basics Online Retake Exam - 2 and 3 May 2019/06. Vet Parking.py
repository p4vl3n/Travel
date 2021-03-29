days = int(input())
hours = int(input())
total_parking_cost = 0
parking_fee = 0
for day in range(1, days + 1):
    daily_parking_cost = 0
    if day % 2 == 0:
        for hour in range(1, hours + 1):
            if hour % 2 == 0:
                parking_fee = 1
            else:
                parking_fee = 2.50
            daily_parking_cost += parking_fee
    else:
        for hour in range(1, hours + 1):
            if hour % 2 == 0:
                parking_fee = 1.25
            else:
                parking_fee = 1
            daily_parking_cost += parking_fee
    total_parking_cost += daily_parking_cost
    print(f'Day: {day} - {daily_parking_cost:.2f} leva')
print(f'Total: {total_parking_cost:.2f} leva')