outcome = []
winner = " "
for line in range(3):
    row = input().split(" ")
    outcome.append(row)
having_a_winner = False
for a, first_el in enumerate(outcome[0]):
    if having_a_winner:
        break
    for b, second_el in enumerate(outcome[1]):
        if having_a_winner:
            break
        for c, third_el in enumerate(outcome[2]):
            if len(set(outcome[0])) == 1 or len(set(outcome[1])) == 1 or len(set(outcome[2])) == 1:
                counter = 0
                while counter < 3:
                    if len(set(outcome[counter])) == 1:
                        winner = outcome[counter][0]
                    counter += 1
                having_a_winner = True
                break
            elif a == b == c and first_el == second_el == third_el:
                winner = first_el
                having_a_winner = True
                break
            elif outcome[0][0] == outcome[1][1] == outcome[2][2] or outcome[2][0] == outcome[1][1] == outcome[0][2]:
                winner = outcome[1][1]
                having_a_winner = True
                break
if winner == "1" and having_a_winner:
    print(f"First player won")
elif winner == "2" and having_a_winner:
    print(f"Second player won")
else:
    print(f"Draw!")