people = int(input())
season = input()
price = 0
if people < 6:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.50 * 0.85
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86 * 1.08
else:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45 * 0.85
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        price = 85 * 1.08
cost = people * price
print(f"{cost:.2f} leva.")
