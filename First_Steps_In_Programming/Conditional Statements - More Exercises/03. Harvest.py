# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.
from math import ceil
from math import floor
area = int(input())
grapes_per_sqm = float(input())
litres_needed = float(input())
workers_count = int(input())
wine_harvest = area * grapes_per_sqm
wine_litres = 0.4 * wine_harvest / 2.5
difference = abs(wine_litres - litres_needed)
if wine_litres >= litres_needed:
    wine_per_person = ceil(difference / workers_count)
    wine_litres = floor(wine_litres)
    difference = ceil(difference)
    print(f'Good harvest this year! Total wine: {wine_litres} liters.')
    print(f'{difference} liters left -> {wine_per_person} liters per person.')
else:
    difference = floor(difference)
    print(f'It will be a tough winter! More {difference} liters wine needed.')
