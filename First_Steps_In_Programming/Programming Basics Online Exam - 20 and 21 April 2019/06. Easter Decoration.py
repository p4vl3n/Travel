customers = int(input())
basket_price = 1.50
wreath_price = 3.80
bunny_price = 7
all_bills = 0
for customer in range(customers):
    purchases = 0
    bill = 0
    purchase = ''
    while purchase != "Finish":
        if purchase == "basket":
            bill += basket_price
        elif purchase == "wreath":
            bill += wreath_price
        elif purchase == "chocolate bunny":
            bill += bunny_price
        purchase = input()
        if purchase == "Finish":
            break
        purchases += 1
    if purchases % 2 == 0:
        bill *= 0.80
    if purchase == "Finish":
        print(f"You purchased {purchases} items for {bill:.2f} leva.")
    all_bills += bill
average = all_bills / customers
print(f"Average bill per client is: {average:.2f} leva.")



