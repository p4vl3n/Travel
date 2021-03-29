budget = float(input())
season = input()
price = 0
accommodation = ""
destination = ""
if season == "summer":
    accommodation = "Camp"
    if budget <= 100:
        price = 0.30 * budget
        destination = "Bulgaria"
    elif 100 < budget <= 1000:
        price = 0.40 * budget
        destination = "Balkans"
    elif budget > 1000:
        price = 0.90 * budget
        destination = "Europe"
        accommodation = "Hotel"
elif season == "winter":
    accommodation = "Hotel"
    if budget <= 100:
        price = 0.70 * budget
        destination = "Bulgaria"
    elif 100 < budget <= 1000:
        price = 0.80 * budget
        destination = "Balkans"
    elif budget > 1000:
        price = 0.90 * budget
        destination = "Europe"
print(f'Somewhere in {destination}')
print(f'{accommodation} - {price:.2f}')