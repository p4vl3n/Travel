from math import sqrt

def find_longer_line(coord_a, coord_b):
    coord_a = [int(x) for x in coord_a]
    coord_b = [int(y) for y in coord_b]
    if coord_a[0] < coord_a[2]:
        side_a = abs(coord_a[0] - coord_a[2])

    line_a = sqrt(abs(coord_a[0])**2 + abs(coord_b[0])**2)
    lien_b = sqrt(abs(coord_a[1[]]))

first_line = []
second_line = []
for coordinate in range(8):
    if coordinate < 4:
        first_line.append(input())
    else:
        second_line.append(input())

