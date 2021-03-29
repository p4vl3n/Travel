count_of_people = int(input())
elevator_capacity = int(input())
trips = 0
if count_of_people < elevator_capacity:
    trips = 1
else:
    if count_of_people % elevator_capacity == 0:
        trips = int(count_of_people / elevator_capacity)
    else:
        trips = (count_of_people // elevator_capacity) + 1

print(trips)