player_one = int(input())
player_two = int(input())
decision = ""
while decision != "End of battle":
    decision = input()
    if decision == "one":
        player_two -= 1
    elif decision == "two":
        player_one -= 1
    if player_one < 1:
        print(f'Player one is out of eggs. Player two has {player_two} eggs left.')
        break
    elif player_two < 1:
        print(f'Player two is out of eggs. Player one has {player_one} eggs left.')
        break
    if decision == "End of battle":
        print(f'Player one has {player_one} eggs left.')
        print(f'Player two has {player_two} eggs left.')

