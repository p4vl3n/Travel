will = float(input())
final_year = int(input())
spend = 0
for year in range(1800, final_year + 1):
    if year % 2 == 0:
        spend += 12000
    else:
        spend += 12000 + 50*(year - 1800 + 18)
if will >= spend:
    print(f'Yes! He will live a carefree life and will have {(will - spend):.2f} dollars left.')
else:
    print(f'He will need {abs(spend-will):.2f} dollars to survive.')
