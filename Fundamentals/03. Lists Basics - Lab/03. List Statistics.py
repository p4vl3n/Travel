lines = int(input())
positives = []
negatives = []
for line in range(lines):
    given_num = int(input())
    if given_num < 0:
        negatives.append(given_num)
    elif given_num > 0:
        positives.append(given_num)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")