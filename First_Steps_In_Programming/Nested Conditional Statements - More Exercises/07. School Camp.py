season = input()
group_type = input()
students_count = int(input())
nights = int(input())
price_per_night = 0
mixed_price_per_night = 0
total_price = 0
sport = 0
if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        price_per_night = 9.60
        if group_type == "boys":
            sport = "Judo"
        elif group_type == "girls":
            sport = "Gymnastics"
    elif season == "Spring":
        price_per_night = 7.20
        if group_type == "boys":
            sport = "Tennis"
        elif group_type == "girls":
            sport = "Athletics"
    elif season == "Summer":
        price_per_night = 15
        if group_type == "boys":
            sport = "Football"
        elif group_type == "girls":
            sport = "Volleyball"
elif group_type == "mixed":
    if season == "Winter":
        price_per_night = 10
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.50
        sport = "Cycling"
    elif season == "Summer":
        price_per_night = 20
        sport = "Swimming"
total_price = price_per_night * students_count * nights
if students_count >= 50:
    total_price *= 0.50
elif 20 <= students_count < 50:
    total_price *= 0.85
elif 10 <= students_count < 20:
    total_price *= 0.95
print(f'{sport} {total_price:.2f} lv.')
