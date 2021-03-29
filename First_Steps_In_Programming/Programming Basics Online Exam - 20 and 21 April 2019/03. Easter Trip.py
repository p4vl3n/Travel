destination = input()
dates = input()
nights = int(input())
night_cost = 0
if destination == "France":
    if dates == "21-23":
        night_cost = 30
    elif dates == "24-27":
        night_cost = 35
    elif dates == "28-31":
        night_cost = 40
elif destination == "Italy":
    if dates == "21-23":
        night_cost = 28
    elif dates == "24-27":
        night_cost = 32
    elif dates == "28-31":
        night_cost = 39
elif destination == "Germany":
    if dates == "21-23":
        night_cost = 32
    elif dates == "24-27":
        night_cost = 37
    elif dates == "28-31":
        night_cost = 43
trip_cost = nights * night_cost
print(f'Easter trip to {destination} : {trip_cost:.2f} leva.')