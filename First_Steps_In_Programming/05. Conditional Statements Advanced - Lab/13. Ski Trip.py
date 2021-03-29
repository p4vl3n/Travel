single_room = 18
apartment = 25
suite = 35
stay = int(input())
room_type = input()
review = input()
nights = stay - 1
final_price = 0
if stay < 10:
    if room_type == "room for one person":
        final_price = nights * single_room
    elif room_type == "apartment":
        final_price = nights * apartment * 0.70
    elif room_type == "president apartment":
        final_price = nights * suite * 0.90
elif 10 <= stay <= 15:
    if room_type == "room for one person":
        final_price = nights * single_room
    elif room_type == "apartment":
        final_price = nights * apartment * 0.65
    elif room_type == "president apartment":
        final_price = nights * suite * 0.85
elif stay > 15:
    if room_type == "room for one person":
        final_price = nights * single_room
    elif room_type == "apartment":
        final_price = nights * apartment * 0.50
    elif room_type == "president apartment":
        final_price = nights * suite * 0.80
if review == "positive":
    final_price *= 1.25
elif review == "negative":
    final_price *= 0.90
print(f'{final_price:.2f}')