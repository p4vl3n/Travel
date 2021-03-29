given_input = input().split("#")
fire_and_cell = [x.split(" = ") for x in given_input]
water = int(input())
low = []
medium = []
high = []
effort = 0
fire = 0
cells_put_out = []
for i in range(1, 126):
    if 1 <= i <= 50:
        low.append(i)
    elif 50 < i <= 80:
        medium.append(i)
    else:
        high.append(i)
for cell, case in enumerate(fire_and_cell):
    cell_was_put_out = False
    if case[0] == "High":
        if int(case[1]) in high and int(case[1]) <= water:
            water -= int(case[1])
            fire += int(case[1])
            effort += 0.25 * int(case[1])
            cell_was_put_out = True
        else:
            continue
    elif case[0] == "Medium":
        if int(case[1]) in medium and int(case[1]) <= water:
            water -= int(case[1])
            fire += int(case[1])
            effort += 0.25 * int(case[1])
            cell_was_put_out = True
        else:
            continue
    elif case[0] == "Low":
        if int(case[1]) in low and int(case[1]) <= water:
            water -= int(case[1])
            fire += int(case[1])
            effort += 0.25 * int(case[1])
            cell_was_put_out = True
    if cell_was_put_out:
        cells_put_out.append(case[1])
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")


