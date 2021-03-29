from math import sqrt


def closer_to_center(lst1, lst2):
    first_line = sqrt(abs(lst1[0])**2 + abs(lst1[1])**2)
    second_line = sqrt(abs(lst2[0])**2 + abs(lst2[1])**2)
    if first_line <= second_line:
        return tuple(lst1)
    return tuple(lst2)


first_coordinates = []
second_coordinates = []
for coordinate in range(2):
    coord = int(input())
    first_coordinates.append(coord)
for other_coord in range(2):
    coord = int(input())
    second_coordinates.append(coord)
print(closer_to_center(first_coordinates, second_coordinates))
