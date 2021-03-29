n = int(input())
music = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    if piece not in music:
        music[piece] = {'composer':composer, 'key': key}
command = input()
while not command == "Stop":
    data = command.split("|")
    action = data[0]
    piece = data[1]
    if action == "Add":
        composer = data[2]
        key = data[3]
        if not piece in music:
            music[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        if piece not in music:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            music.pop(piece, None)
            print(f"Successfully removed {piece}!")
    elif action == "ChangeKey":
        key = data[2]
        if piece not in music:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            key = data[2]
            music[piece]['key'] = key
            print(f"Changed the key of {piece} to {key}!")
    command = input()


new_music = dict(sorted(music.items(), key= lambda x: (x[0], x[1]['composer'])))
for piece in new_music:
    print(f"{piece} -> Composer: {new_music[piece]['composer']}, Key: {new_music[piece]['key']}")