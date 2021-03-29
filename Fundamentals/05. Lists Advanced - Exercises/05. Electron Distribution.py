electrons_count = int(input())
positioned_electrons = []
index = 1
while electrons_count > 0:
    electrons_in_position = 2*index**2
    index += 1
    if electrons_in_position <= electrons_count:
        positioned_electrons.append(electrons_in_position)
        electrons_count -= electrons_in_position
    else:
        positioned_electrons.append(electrons_count)
        electrons_count = 0
print(positioned_electrons)