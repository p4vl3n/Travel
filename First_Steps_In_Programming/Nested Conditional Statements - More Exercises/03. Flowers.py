chrysanthemum = 0
rose = 0
tulip = 0
chrys_count = int(input())
rose_count = int(input())
tulip_count = int(input())
season = input()
holiday = input()
all_flowers = chrys_count + rose_count + tulip_count
if season == "Spring" or season == "Summer":
    chrysanthemum = 2.00
    rose = 4.10
    tulip = 2.50
    if holiday == "Y":
        chrysanthemum += 0.15 * chrysanthemum
        rose += 0.15 * rose
        tulip += 0.15 * tulip
    if season == "Spring" and tulip_count > 7:
        chrysanthemum -= 0.05 * chrysanthemum
        rose -= 0.05 * rose
        tulip -= 0.05 * tulip
elif season == "Autumn" or season == "Winter":
    chrysanthemum = 3.75
    rose = 4.50
    tulip = 4.15
    if holiday == "Y":
        chrysanthemum += 0.15 * chrysanthemum
        rose += 0.15 * rose
        tulip += 0.15 * tulip
    if season == "Winter" and rose_count >= 10:
        chrysanthemum -= 0.10 * chrysanthemum
        rose -= 0.10 * rose
        tulip -= 0.10 * tulip
buquet = tulip * tulip_count + rose * rose_count + chrysanthemum * chrys_count
if all_flowers > 20:
    buquet -= 0.20 * buquet
buquet += 2
print(f'{buquet:.2f}')