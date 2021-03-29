gasoline = 2.22
diesel = 2.33
lpg = 0.93
fuel_type = input()
fuel_quantity = int(input())
club_card = input()
if club_card == "Yes":
    gasoline -= 0.18
    diesel -= 0.12
    lpg -= 0.08
    gasoline_cost = gasoline * fuel_quantity
    diesel_cost = diesel * fuel_quantity
    lpg_cost = lpg * fuel_quantity
    if fuel_quantity > 25:
        lpg_cost *= 0.90
        gasoline_cost *= 0.90
        diesel_cost *= 0.90
        if fuel_type == "Gas":
            print(f'{lpg_cost:.2f} lv.')
        elif fuel_type == "Gasoline":
            print(f'{gasoline_cost:.2f} lv.')
        elif fuel_type == "Diesel":
            print(f'{diesel_cost:.2f} lv.')
    elif fuel_quantity >= 20:
        lpg_cost *= 0.92
        gasoline_cost *= 0.92
        diesel_cost *= 0.92
        if fuel_type == "Gas":
            print(f'{lpg_cost:.2f} lv.')
        elif fuel_type == "Gasoline":
            print(f'{gasoline_cost:.2f} lv.')
        elif fuel_type == "Diesel":
            print(f'{diesel_cost:.2f} lv.')
    else:
        if fuel_type == "Gas":
            print(f'{lpg_cost:.2f} lv.')
        elif fuel_type == "Gasoline":
            print(f'{gasoline_cost:.2f} lv.')
        elif fuel_type == "Diesel":
            print(f'{diesel_cost:.2f} lv.')
else:
    gasoline_cost = gasoline * fuel_quantity
    diesel_cost = diesel * fuel_quantity
    lpg_cost = lpg * fuel_quantity
    if fuel_quantity > 25:
        lpg_cost *= 0.90
        gasoline_cost *= 0.90
        diesel_cost *= 0.90
        if fuel_type == "Gas":
            print(f'{lpg_cost:.2f} lv.')
        elif fuel_type == "Gasoline":
            print(f'{gasoline_cost:.2f} lv.')
        elif fuel_type == "Diesel":
            print(f'{diesel_cost:.2f} lv.')
    elif fuel_quantity >= 20:
        lpg_cost *= 0.92
        gasoline_cost *= 0.92
        diesel_cost *= 0.92
        if fuel_type == "Gas":
            print(f'{lpg_cost:.2f} lv.')
        elif fuel_type == "Gasoline":
            print(f'{gasoline_cost:.2f} lv.')
        elif fuel_type == "Diesel":
            print(f'{diesel_cost:.2f} lv.')
    else:
        if fuel_type == "Gas":
            print(f'{lpg_cost:.2f} lv.')
        elif fuel_type == "Gasoline":
            print(f'{gasoline_cost:.2f} lv.')
        elif fuel_type == "Diesel":
            print(f'{diesel_cost:.2f} lv.')
