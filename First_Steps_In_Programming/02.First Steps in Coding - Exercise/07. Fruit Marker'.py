strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())
raspberries_price = strawberries_price / 2
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price
banana_money = bananas_price * bananas_quantity
orange_money = oranges_quantity * oranges_price
raspberry_money = raspberries_quantity * raspberries_price
strawberry_money = strawberries_quantity * strawberries_price
print(banana_money + orange_money + raspberry_money + strawberry_money)