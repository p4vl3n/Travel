lines = int(input())

positives = []
negatives = []
evens = []
odds = []

for line in range(lines):
    given_int = int(input())
    if given_int >= 0:
        positives.append(given_int)
    else:
        negatives.append(given_int)
    if given_int % 2 == 0:
        evens.append(given_int)
    else:
        odds.append(given_int)

call_out = input()
if call_out == "positive":
    print(positives)
elif call_out == "negative":
    print(negatives)
elif call_out == "even":
    print(evens)
elif call_out == "odd":
    print(odds)
