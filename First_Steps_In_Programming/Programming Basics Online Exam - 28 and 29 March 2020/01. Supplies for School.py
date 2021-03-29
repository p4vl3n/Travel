pack_of_pens = 5.80
pack_of_markers = 7.20
detergent_per_liter = 1.20
pen_packs = int(input())
marker_packs = int(input())
liters_of_detergent = float(input())
discount = int(input())
total_sum = pack_of_pens * pen_packs + liters_of_detergent * detergent_per_liter + pack_of_markers * marker_packs
discounted_sum = total_sum - total_sum * discount / 100
print(f'{discounted_sum:.3f}')
