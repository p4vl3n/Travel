dollar = 1.76
euro = 1.95
bitcoin = 1168
yuan = 0.15 * dollar
bitcoin_count = int(input())
yuan_count = float(input())
comission = float(input())
total_euro = (bitcoin_count * bitcoin + yuan_count * yuan) / euro
to_receive = total_euro - comission / 100 * total_euro
print(f'{to_receive:.2f}')