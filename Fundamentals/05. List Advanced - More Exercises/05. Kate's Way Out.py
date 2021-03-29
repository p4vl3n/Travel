maze_rows = int(input())
maze = []

for _ in range(maze_rows):
    row = list(input())
    maze.append(row)

kate = 0
level = 0
moves = 0
there_is_way_out = True

for row in range(len(maze) - 1, 0, -1):
    if not there_is_way_out:
        break
    for position in range(len(maze[row])):
        if not maze[row][position] == "#" and not maze[row][position] == "k":
            there_is_way_out = True
            break
        else:
            there_is_way_out = False

if there_is_way_out:
    rows = []
    for row in range(len(maze)):
        empty_spaces = []
        for position in range(len(maze[row])):
            if maze[row][position] == "k":
                kate = position
                level = row
            elif not maze[row][position] == "#":
                empty_spaces.append(position)
        rows.append(empty_spaces)
    while level in range(len(rows)):
        if len(rows) > level + 1:
            for space in rows[level + 1]:
                if space in rows[level]:
                    if kate == space:
                        moves += 1
                    else:
                        moves = abs(kate - space) + 1
                    kate = space
        else:
            moves += 1
        level += 1

    print(f"Kate got out in {moves} moves")
else:
    print(f"Kate cannot get out")
