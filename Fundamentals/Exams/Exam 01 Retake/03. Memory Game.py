elements = input().split()
command_data = input()
moves = 0
won_the_game = False
while not command_data == "end":
    moves += 1
    first, second = map(int, command_data.split())
    if first == second or first >= len(elements) or second >= len(elements) or first < 0 or second < 0:
        if len(elements):
            print(f"Invalid input! Adding additional elements to the board")
            position = int(len(elements) / 2)
            new_element = f"-{moves}a"
            for _ in range(2):
                elements.insert(position, new_element)
    elif elements[first] == elements[second]:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        to_remove = [elements[first], elements[second]]
        elements = [element for element in elements if element not in to_remove]
        if not len(elements):
            print(f"You have won in {moves} turns!")
            won_the_game = True
    elif not elements[first] == elements[second]:
        print(f"Try again!")
    command_data = input()
if not won_the_game:
    print(f"Sorry you lose :(")
    print(*elements)
