width = int(input())
length = int(input())
height = int(input())
room_volume = width * length * height
command = input()
moved_boxes_volume = 0
while command != "Done":
    boxes = int(command)
    moved_boxes_volume += boxes
    difference = abs(room_volume - moved_boxes_volume)
    if room_volume < moved_boxes_volume:
        print(f'No more free space! You need {difference} Cubic meters more.')
        break
    command = input()
else:
    print(f'{difference} Cubic meters left.')
