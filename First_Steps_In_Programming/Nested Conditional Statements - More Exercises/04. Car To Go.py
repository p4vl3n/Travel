budget = float(input())
season = input()
car_class = 0
if budget <= 100:
    car_class = "Economy class"
    summer_car_price = 0.35 * budget
    winter_car_price = 0.65 * budget
elif 100 < budget <= 500:
    car_class = "Compact class"
    summer_car_price = 0.45 * budget
    winter_car_price = 0.80 * budget
elif budget > 500:
    car_class = "Luxury class"
    car_price = 0.90 * budget
if season == "Summer" and budget <= 500:
    print(car_class)
    print(f'Cabrio - {summer_car_price:.2f}')
elif season == "Winter" and budget <= 500:
    print(car_class)
    print(f'Jeep - {winter_car_price:.2f}')
else:
    print(car_class)
    print(f'Jeep - {car_price:.2f}')
