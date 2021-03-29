class Car:
    def __init__(self, car_name: str, mileage: int, fuel: int):
        self.car_name = car_name
        self.mileage = mileage
        self.fuel = fuel


n = int(input())
garage = []

for _ in range(n):
    car_name, mileage, fuel = input().split("|")   
    car = Car(car_name, int(mileage), int(fuel))
    garage.append(car)

command = input()

while not command == "Stop":
    data = command.split(" : ")
    action, car_name = data[0], data[1]
    car = [auto for auto in garage if auto.car_name == car_name][0]
    if action == "Drive":
        distance, used_fuel = int(data[2]), int(data[3])
        if used_fuel <= car.fuel:
            car.fuel -= used_fuel
            car.mileage += distance
            print(f"{car_name} driven for {distance} kilometers. {used_fuel} liters of fuel consumed.")
            if car.mileage > 99999:
                print(f"Time to sell the {car_name}!")
                garage.remove(car)
        else:
            print(f"Not enough fuel to make that ride")
    elif action == "Refuel":
        new_fuel = int(data[2])
        if new_fuel + car.fuel > 75:
            new_fuel = 75 - car.fuel
        car.fuel += new_fuel
        print(f"{car_name} refueled with {new_fuel} liters")
    elif action == "Revert":
        kilometers = int(data[2])
        car.mileage -= kilometers
        if car.mileage < 10000:
            car.mileage = 10000
        else:
            print(f"{car_name} mileage decreased by {kilometers} kilometers")
    command = input()

sorted_garage = sorted(garage, key= lambda car: (-car.mileage, car.car_name))
for auto in sorted_garage:
    print(f"{auto.car_name} -> Mileage: {auto.mileage} kms, Fuel in the tank: {auto.fuel} lt.") 
