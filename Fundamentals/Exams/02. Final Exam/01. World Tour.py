trip = input()
command = input()
while not command == "Travel":
    action, index_location, new_info = command.split(":")
    if action == "Add Stop":
        index_location = int(index_location)
        if 0 <= index_location < len(trip):
            remodeled_string = trip[:index_location] + new_info + trip[index_location:]
            trip = remodeled_string
        print(trip)
    elif action == "Remove Stop":
        index_location = int(index_location)
        if 0 <= index_location < len(trip) and 0 <= int(new_info) < len(trip):
            remodeled_string = trip[:index_location] + trip[int(new_info) + 1:]
            trip = remodeled_string
        print(trip)
    elif action == "Switch":
        trip = trip.replace(index_location, new_info)
        print(trip)


    command = input()
print(f"Ready for world tour! Planned stops: {trip}")