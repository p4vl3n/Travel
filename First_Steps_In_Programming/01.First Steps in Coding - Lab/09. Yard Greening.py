price_per_sqm = float(7.61)
yard = float(input())
quote = yard * price_per_sqm
discount = float(0.18 * quote)
final_price = float(quote - discount)
print(f"The final price is {final_price}")
print(f"The discount is {discount}")