budget = float(input())
crew = int(input())
costume_price = float(input())
decor = budget * 0.10
if crew > 150:
    costume_price *= 0.90
costume_budget = crew * costume_price
required_budget = costume_budget + decor
difference = abs(required_budget - budget)
if required_budget > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")