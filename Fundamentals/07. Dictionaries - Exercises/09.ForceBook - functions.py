force = {}
final = {}
text = input()
while not text == "Lumpawaroo":
    if " | " in text:
        side = text.split(" | ")[0]
        user = text.split(" | ")[1]
        if user not in force:
            force[user] = side
    elif " -> " in text:
        user = text.split(" -> ")[0]
        side = text.split(" -> ")[1]
        force[user] = side
        print(f"{user} joins the {side} side!")

    text = input()

for user, side in force.items():
        if side not in final:
            final[side] = []
        final[side].append(user)

sorted_finals = dict(sorted(final.items(), key = lambda x: (-len(x[1]), x[0])))

for side, members in sorted_finals.items():
    members.sort()
    print(f"Side: {side}, Members: {len(members)}")
    [print(f"! {member}") for member in members]
        