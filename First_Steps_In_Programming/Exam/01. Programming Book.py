price_per_page = float(input())
price_per_cover = float(input())
discount = int(input())
designer_pay = float(input())
percentage_to_pay_team = int(input())
pages = 899
covers = 2
total_cost = pages * price_per_page + price_per_cover * covers
discounted_cost = total_cost - (discount/100 * total_cost)
total_to_pay = discounted_cost + designer_pay
paid_by_team = percentage_to_pay_team * total_to_pay / 100
final_pay = total_to_pay - paid_by_team
print(f"Avtonom should pay {final_pay:.2f} BGN.")