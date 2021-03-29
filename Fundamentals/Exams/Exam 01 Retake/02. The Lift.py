people = int(input())
lift = list(map(int, input().split()))
empty_seats = True
for wagon in range(len(lift)):
    if lift[wagon] == 0:
        if people >= 4:
            lift[wagon] += 4
            people -= 4
        else:
            lift[wagon] += people
            people -= people
    else:
        capacity = 4 - lift[wagon]
        if people >= capacity:
            lift[wagon] += capacity
            people -= capacity
        else:
            lift[wagon] += people
            people -= people
for wagon in lift:
    if wagon < 4:
        empty_seats = True
    else:
        empty_seats = False
if empty_seats:
    print("The lift has empty spots!")
    print(*lift)
else:
    if people:
        print(f"There isn't enough space! {people} people in a queue!")
        print(*lift)
    else:
        print(*lift)