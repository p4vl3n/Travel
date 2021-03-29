def fight(plr_one, plr_two, skills):
    if skills[plr_one] < skills[plr_two]:
        return plr_one
    elif skills[plr_one] > skills[plr_two]:
        return plr_two
    return None


players_total_skill = {}
player_skill_and_score = {}
command = input()
while not command == "Season end":
    if "vs" in command:
        player_one = command.split(" vs ")[0]
        player_two = command.split(" vs ")[1]
        if player_one in player_skill_and_score and player_two in player_skill_and_score:
           for skill, score in player_skill_and_score[player_one].items():
               if skill in player_skill_and_score[player_two]:
                    loser = fight(player_one, player_two, players_total_skill)
                    if loser is None:
                       break
                    else:
                        player_skill_and_score.pop(loser)
                        players_total_skill.pop(loser)

    else:
        player, skill, score = command.split(" -> ")
        score = int(score)
        if player not in player_skill_and_score:
            player_skill_and_score[player] = {skill: score}
            players_total_skill[player] = score
        else:
            if skill not in player_skill_and_score[player]:
                player_skill_and_score[player][skill] = score
                players_total_skill[player] += score
            else:
                if score > player_skill_and_score[player][skill]:
                    diff = player_skill_and_score[player][skill] - score
                    player_skill_and_score[player][skill] = score
                    players_total_skill[player] += diff

    command = input()
sorted_skills = dict(sorted(players_total_skill.items(), key=lambda x: -x[1]))
for player in player_skill_and_score:
   player_skill_and_score[player] = dict(sorted(player_skill_and_score[player].items(), key=lambda x: (-x[1], x[0])))
for player, score in sorted_skills.items():
    print(f"{player}: {score} skill")
    for skill, score in player_skill_and_score[player].items():
        print(f"- {skill} <::> {score}")
