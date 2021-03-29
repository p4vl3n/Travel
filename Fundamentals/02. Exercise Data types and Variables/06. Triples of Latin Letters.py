num = int(input())
for a in range(97, 97 + num):
    for b in range(97, 97 + num):
        for c in range(97, 97 + num):
            print(f"{chr(a)}{chr(b)}{chr(c)}")