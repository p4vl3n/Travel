flavor = input()
size = input()
set_orders = int(input())
price = 0
total_price = 0
if size == "small":
    if flavor == "Watermelon":
        price = 56 * 2
    elif flavor == "Mango":
        price = 36.66 * 2
    elif flavor == "Pineapple":
        price = 42.10 * 2
    elif flavor == "Raspberry":
        price = 20 * 2
    total_price = price * set_orders
elif size == "big":
    if flavor == "Watermelon":
        price = 28.70 * 5
    elif flavor == "Mango":
        price = 19.60 * 5
    elif flavor == "Pineapple":
        price = 24.80 * 5
    elif flavor == "Raspberry":
        price = 15.20 * 5
    total_price = price * set_orders
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
print(f'{total_price:.2f} lv.')