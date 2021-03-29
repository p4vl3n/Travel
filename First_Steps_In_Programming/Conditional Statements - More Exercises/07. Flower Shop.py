from math import floor
from math import ceil
magnolia = 3.25
zumbul = 4
rose = 3.5
cactus = 8
magnolia_count = int(input())
zumbul_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_cost = float(input())
order_revenue = 0.95 * (magnolia * magnolia_count + zumbul * zumbul_count + rose * rose_count + cactus * cactus_count)
difference = abs(gift_cost - order_revenue)
if order_revenue >= gift_cost:
    difference = floor(difference)
    print(f'She is left with {difference} leva.')
else:
    difference = ceil(difference)
    print(f'She will have to borrow {difference} leva.')
