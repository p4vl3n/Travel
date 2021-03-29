skumria_price = float(input())
caca_price = float(input())

palamud_quantity = float(input())
palamud_price = 0.6 * skumria_price + skumria_price
palamud_purchase = palamud_price * palamud_quantity

safrid_quantity = float(input())
safrid_price = 0.8 * caca_price + caca_price
safrid_purchase = safrid_price * safrid_quantity

midi_quantity = float(input())
midi_price = 7.50
midi_purchase = midi_price * midi_quantity

total_spent = palamud_purchase + safrid_purchase + midi_purchase
print(round(total_spent, 2))


