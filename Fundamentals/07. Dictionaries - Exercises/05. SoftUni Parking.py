parking_lot = {}
users = int(input())
for user in range(users):
    command = input()
    register = command.split()[0]
    username = command.split()[1]
    if register == "register":
        license_plate = command.split()[2]
        if username not in parking_lot:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
    elif register == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking_lot.pop(username)

for user, plate in parking_lot.items():
    print(f"{user} => {plate}")