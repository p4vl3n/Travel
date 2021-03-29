# Лили вече е на N години.
# За нечетните рождени дни получава играчки, а за всеки четен получава пари.
age = int(input())
gifts = 0
savings = 0
birthday_money = 0

for year in range(age + 1):
    if year >= 1 and (year % 2 != 0):
        gifts += 1
    elif year > 1 and (year % 2 == 0):
        birthday_money += 10
        savings += birthday_money
        savings -= 1
washer_price = float(input())
gift_price = int(input())
savings += gifts * gift_price
difference = abs(savings - washer_price)
if savings >= washer_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')



# За втория рожден ден получава 10.00 лв,
# като сумата се увеличава с 10.00 лв., за всеки следващ четен рожден ден (2 -&gt; 10, 4 -&gt; 20, 6 -&gt; 30...и т.н.).
# Братът на Лили, в годините, които тя получава пари, взима
# по 1.00 лев от тях.Лили продала играчките получени през годините, всяка за P лева и добавила сумата към
# спестените пари.С парите искала да си купи пералня за X лева. Напишете програма, която да пресмята,
# # колко пари е събрала и дали ѝ стигат да си купи пералня.