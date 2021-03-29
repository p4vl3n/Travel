veggie_price = float(input())
fruits_price = float(input())
veggie_kg = float(input())
fruits_kg = float(input())
income_lv = veggie_price * veggie_kg + fruits_price * fruits_kg
income_euro = income_lv / 1.94
print(f'{income_euro:.2f}')