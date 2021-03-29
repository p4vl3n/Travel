force = {}
command = input()
while not command == "Lumpawaroo":
    if "|" in command:
        command_data = command.split(" | ")
        side = command_data[0]
        member = command_data[1]
        if side not in force:
            force[side] = []
        if member not in force[side]:
            force.get(side).append(member)
    elif "->" in command:
        command_data = command.split(" -> ")
        member = command_data[0]
        side = command_data[1]
        if side in force.keys():
            for opposite_side in force.keys():
                if not opposite_side == side:
                    if member in force.get(opposite_side):
                        force.get(opposite_side).remove(member)
            force.get(side).append(member)
        else:
            force[side] = member
        print(f"{member} joins the {side} side!")    
    command = input()
sorted_forces = dict(sorted(force.items(), key=lambda kvp: (-len(kvp[1]), (kvp[0]))))

for side, members in sorted_forces.items():
    sorted_forces[side] = sorted(members)
    if not len(members):
        continue
    else:
        print(f"Side: {side}, Members: {len(members)}")
        for member in sorted_forces.get(side):
            print(f"! {member}")
