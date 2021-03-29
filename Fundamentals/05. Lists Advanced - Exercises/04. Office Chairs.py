rooms = int(input())
enough_chairs = True
free_chairs = 0
for room in range(1, rooms + 1):
    chairs_and_people = input().split()
    if len(chairs_and_people[0]) < int(chairs_and_people[1]):
        print(f"{int(chairs_and_people[1]) - len(chairs_and_people[0])} more chairs needed in room {room}")
        enough_chairs = False
    else:
        free_chairs += len(chairs_and_people[0]) - int(chairs_and_people[1])
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

