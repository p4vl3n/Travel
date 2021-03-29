stage = input()
type_of_ticket = input()
tickets = int(input())
trophy_picture = input()
free_picture = False
price = 0
picture_price = 40
picture_cost = 0
if stage == "Quarter final":
    if type_of_ticket == "Standard":
        price = 55.50
    elif type_of_ticket == "Premium":
        price = 105.20
    elif type_of_ticket == "VIP":
        price = 118.90
elif stage == "Semi final":
    if type_of_ticket == "Standard":
        price = 75.88
    elif type_of_ticket == "Premium":
        price = 125.22
    elif type_of_ticket == "VIP":
        price = 300.40
elif stage == "Final":
    if type_of_ticket == "Standard":
        price = 110.10
    elif type_of_ticket == "Premium":
        price = 160.66
    elif type_of_ticket == "VIP":
        price = 400
total_cost = tickets * price
if total_cost > 4000:
    total_cost *= 0.75
    free_picture = True
elif total_cost > 2500:
    total_cost *= 0.90
if trophy_picture == "Y":
    picture_cost = tickets * picture_price
if free_picture:
    print(f"{total_cost:.2f}")
else:
    print(f"{total_cost + picture_cost:.2f}")
