budget = float(input())
season = input()
hotel = 0
alaska_budget = 0
morocco_budget = 0
if budget <= 1000:
    hotel = "Camp"
    alaska_budget = 0.65 * budget
    morocco_budget = 0.45 * budget
elif 1000 < budget <= 3000:
    hotel = "Hut"
    alaska_budget = 0.80 * budget
    morocco_budget = 0.60 * budget
elif budget > 3000:
    hotel = "Hotel"
    alaska_budget = 0.90 * budget
    morocco_budget = 0.90 * budget
if season == "Summer":
    print(f'Alaska - {hotel} - {alaska_budget:.2f}')
elif season == "Winter":
    print(f'Morocco - {hotel} - {morocco_budget:.2f}')
