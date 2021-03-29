visitors = int(input())
back = 0
chest = 0
legs = 0
abdominals = 0
protein_shake = 0
protein_bar = 0
for visitor in range(visitors):
    action = input()
    if action == "Back":
        back += 1
    elif action == "Chest":
        chest += 1
    elif action == "Legs":
        legs += 1
    elif action == "Abs":
        abdominals += 1
    elif action == "Protein shake":
        protein_shake += 1
    elif action == "Protein bar":
        protein_bar += 1
working_out = back + chest + legs + abdominals
protein_purchases = protein_bar + protein_shake
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abdominals} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{working_out / visitors * 100:.2f}% - work out")
print(f"{protein_purchases / visitors * 100:.2f}% - protein")

