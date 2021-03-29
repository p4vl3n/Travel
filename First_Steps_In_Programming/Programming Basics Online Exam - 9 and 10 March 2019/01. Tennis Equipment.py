from math import ceil
from math import floor
racket_price = float(input())
racket_count = int(input())
sneakers_count = int(input())
sneakers_price = racket_price / 6
racket_sneakers_cost = racket_count * racket_price + sneakers_count * sneakers_price
equipment_cost = 0.20 * racket_sneakers_cost
total_cost = racket_sneakers_cost + equipment_cost
Djokovic_pays = total_cost / 8
Sponsor_pays = total_cost - Djokovic_pays
print(f"Price to be paid by Djokovic {floor(Djokovic_pays)}")
print(f"Price to be paid by sponsors {ceil(Sponsor_pays)}")