command = ""
coffee_count = 0
while command != "END":
    command = input()
    if command == "dog" or command == "cat" or command == "coding" or command == "movie":
        coffee_count += 1
    elif command == "DOG" or command == "CAT" or command == "CODING" or command == "MOVIE":
        coffee_count += 2
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)