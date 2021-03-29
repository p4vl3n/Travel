gifts = list(map(int, input().split(", ")))
count_of_beggars = int(input())
beggars = []
for beggar in range(count_of_beggars):
    beggars.append(0)

for beggar in range(len(beggars)):
    for gift in range(beggar, len(gifts), count_of_beggars):
        beggars[beggar] += gifts[gift]
print(beggars)

