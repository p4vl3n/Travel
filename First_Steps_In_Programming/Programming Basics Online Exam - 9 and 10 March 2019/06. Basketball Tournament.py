tournament = input()
games_played = 0
games_won = 0
games_lost = 0
while tournament != "End of tournaments":
    games_per_tournament = int(input())
    for game in range(1, games_per_tournament + 1):
        games_played += 1
        home_team = int(input())
        away_team = int(input())
        difference = abs(home_team - away_team)
        if home_team > away_team:
            games_won += 1
            print(f"Game {game} of tournament {tournament}: win with {difference} points.")
        elif home_team < away_team:
            games_lost += 1
            print(f"Game {game} of tournament {tournament}: lost with {difference} points.")
    tournament = input()
percentage_won = games_won / games_played * 100
percentage_lost = games_lost / games_played * 100
print(f"{percentage_won:.2f}% matches win")
print(f"{percentage_lost:.2f}% matches lost")