team = input()
souvenir = input()
bought_souvenirs = int(input())
price = 0
invalid_team = False
invalid_souvenir = False
if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
    else:
        invalid_souvenir = True
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
    else:
        invalid_souvenir = True
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
    else:
        invalid_souvenir = True
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
    else:
        invalid_souvenir = True
else:
    invalid_team = True
cost = bought_souvenirs * price
if invalid_team:
    print(f"Invalid country!")
elif invalid_souvenir:
    print(f"Invalid stock!")
else:
    print(f"Pepi bought {bought_souvenirs} {souvenir} of {team} for {cost:.2f} lv.")