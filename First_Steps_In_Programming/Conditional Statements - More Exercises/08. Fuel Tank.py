fuel = input()
fuel_quantity = int(input())
success_message = "You have enough " + fuel + "."
no_success_message = "Fill your tank with " + fuel + "!"
if fuel == "Diesel":
    if fuel_quantity >= 25:
        print(success_message)
    else:
        print(no_success_message)
elif fuel == "Gasoline":
    if fuel_quantity >= 25:
        print(success_message)
    else:
        print(no_success_message)
elif fuel == "Gas":
    if fuel_quantity >= 25:
        print(success_message)
    else:
        print(no_success_message)
else:
    print("Invalid fuel!")

