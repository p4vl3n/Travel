distance = int(input())
time_of_day = input()
taxi_fare = 0.79
bus_fare = 0.09
train_fare = 0.06
if distance < 20:
    if time_of_day == "night":
        taxi_fare = 0.9
        price = distance * taxi_fare + 0.70
        print(f'{price:.2f}')
    else:
        price = distance * taxi_fare + 0.70
        print(f'{price:.2f}')
elif distance >= 100:
    price = train_fare * distance
    print(f'{price:.2f}')
else:
    price = bus_fare * distance
    print(f'{price:.2f}')