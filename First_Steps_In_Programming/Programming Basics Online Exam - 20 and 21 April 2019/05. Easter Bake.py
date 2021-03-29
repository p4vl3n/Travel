import math
import sys
sugar_pack_quantity = 950
flour_pack_quantity = 750
total_used_sugar = 0
total_used_flour = 0
max_flour = - sys.maxsize
max_sugar = - sys.maxsize
breads = int(input())
for bread in range(breads):
    sugar = int(input())
    flour = int(input())
    total_used_sugar += sugar
    total_used_flour += flour
    if sugar >= max_sugar:
        max_sugar = sugar
    if flour >= max_flour:
        max_flour = flour
sugar_packs = math.ceil(total_used_sugar / sugar_pack_quantity)
flour_packs = math.ceil(total_used_flour / flour_pack_quantity)
print(f'Sugar: {sugar_packs}')
print(f"Flour: {flour_packs}")
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
