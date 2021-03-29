starting_score = 301
name = input()
shots = 0
unsuccessful_shots = 0
player_has_retired = False
while starting_score > 0:
    field = input()
    if field == "Retire":
        player_has_retired = True
        break
    score = int(input())
    if field == "Double":
        score *= 2
    elif field == "Triple":
        score *= 3
    if score > starting_score:
        unsuccessful_shots += 1
        continue
    else:
        shots += 1
        starting_score -= score
if player_has_retired:
    print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{name} won the leg with {shots} shots.")
