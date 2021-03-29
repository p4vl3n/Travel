groups = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0
for group in range(groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group < 13:
        mont_blanc += people_in_group
    elif people_in_group < 26:
        kilimanjaro += people_in_group
    elif people_in_group < 41:
        k2 += people_in_group
    else:
        everest += people_in_group
musala_percentage = musala / total_people * 100
mont_blanc_percentage = mont_blanc / total_people * 100
kilimanjaro_percentage = kilimanjaro / total_people * 100
k2_percentage = k2 / total_people * 100
everest_percentage = everest / total_people * 100
print(f'{musala_percentage:.2f}%')
print(f'{mont_blanc_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')