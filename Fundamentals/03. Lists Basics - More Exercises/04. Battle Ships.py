rows = int(input())
fleet = []
attacks = []
destroyed = 0
for row in range(rows):
    given_string = input().split(" ")
    ship = [int(i) for i in given_string]
    fleet.append(ship)
command = input().split(" ")

for element in command:
    attacks.append(element.split("-"))
for i, attack in enumerate(attacks):
    row = int(attack[0])
    col = int(attack[1])
    if fleet[row][col] >= 1:
        fleet[row][col] -= 1
        if not fleet[row][col]:
            destroyed += 1
print(destroyed)
