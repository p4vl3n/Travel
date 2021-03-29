width = int(input())
length = int(input())
total_cake = width * length
cake_is_eaten = False
command = input()
while command != "STOP":
    taken_pieces = int(command)
    total_cake -= taken_pieces
    if total_cake <= 0:
        cake_is_eaten = True
        break
    command = input()
if cake_is_eaten:
    print(f'No more cake left! You need {abs(total_cake)} pieces more.')
else:
    print(f'{total_cake} pieces are left.')

