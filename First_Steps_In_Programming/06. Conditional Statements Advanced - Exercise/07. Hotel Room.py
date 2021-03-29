# Хотел предлага 2 вида стаи: студио и апартамент.
# Напишете програма, която изчислява цената за целия престой за студио и апартамент.
# Цените зависят от месеца на престоя:
# Май и октомври	            Юни и септември	                    Юли и август
# Студио – 50 лв./нощувка	    Студио – 75.20 лв./нощувка	        Студио – 76 лв./нощувка
# Апартамент – 65 лв./нощувка	Апартамент – 68.70 лв./нощувка	    Апартамент – 77 лв./нощувка
##⦁	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# ⦁	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# ⦁	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# ⦁	За апартамент, при повече от 14 нощувки, без значение от месеца : 10%
month = input()
nights_stay = int(input())
studio = 0
apartment = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights_stay <= 14:
        studio *= 0.95
    elif nights_stay > 14:
        studio *= 0.70
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights_stay > 14:
        studio *= 0.80
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
if nights_stay > 14:
    apartment *= 0.90
studio_price = nights_stay * studio
apartment_price = nights_stay * apartment
print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
