length = float(input())
convert_from = input()
convert_to = input()
convertion = 0
if convert_from == "mm":
    if convert_to == "cm":
        convertion = length / 10
    elif convert_to == "m":
        convertion = length / 1000
elif convert_from == "cm":
    if convert_to == "mm":
        convertion = length * 10
    elif convert_to == "m":
        convertion = length / 10
elif convert_from == "m":
    if convert_to == "mm":
        convertion = length * 1000
    elif convert_to == "cm":
        convertion = length * 100

print(f"{convertion:.3f}")
