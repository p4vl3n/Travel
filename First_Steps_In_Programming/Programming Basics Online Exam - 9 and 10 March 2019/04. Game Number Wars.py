player_one = input()
player_two = input()
card_player_one = ""
score_player_one = 0
score_player_two = 0
game_has_ended = False
gone_into_number_wars = False
player_one_is_a_winner = False
player_two_is_a_winner = False
while card_player_one != "End of game":
    card_player_one = input()
    if card_player_one == "End of game":
        game_has_ended = True
        break
    card_player_two = int(input())
    card_player_one = int(card_player_one)
    if card_player_one > card_player_two:
        score_player_one += card_player_one - card_player_two
    elif card_player_two > card_player_one:
        score_player_two += card_player_two - card_player_one
    else:
        gone_into_number_wars = True
        new_card_player_one = int(input())
        new_card_player_two = int(input())
        if new_card_player_one > new_card_player_two:
            player_one_is_a_winner = True
        else:
            player_two_is_a_winner = True
        break
if game_has_ended:
    print(f"{player_one} has {score_player_one} points")
    print(f"{player_two} has {score_player_two} points")
else:
    if player_one_is_a_winner:
        print(f"Number wars!")
        print(f"{player_one} is winner with {score_player_one} points")
    elif player_two_is_a_winner:
        print(f"Number wars!")
        print(f"{player_two} is winner with {score_player_two} points")