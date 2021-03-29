count_of_easter_breads = int(input())
highest_score = 0
winner = ""
for bread in range(count_of_easter_breads):
    baker = input()
    score = input()
    current_score = 0
    while score != "Stop":
        points = int(score)
        current_score += points
        score = input()
    print(f"{baker} has {current_score} points.")
    if current_score > highest_score:
        highest_score = current_score
        winner = baker
        print(f'{baker} is the new number 1!')
print(f"{winner} won competition with {highest_score} points!")