a_team = []
b_team = []
players = 11
for player in range(1, players + 1):
    a_team.append(f"A-{player}")
    b_team.append(f"B-{player}")
players_sent_off = input().split(" ")
set(players_sent_off)
for player in players_sent_off:
    if player in a_team:
        a_team.remove(player)
    elif player in b_team:
        b_team.remove(player)
    if len(a_team) < 7 or len(b_team) < 7:
        break
print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if len(a_team) < 7 or len(b_team) < 7:
    print("Game was terminated")
