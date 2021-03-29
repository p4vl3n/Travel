loads_count = int(input())
bus_price = 200
truck_price = 175
train_price = 120
tons_bus_transport = 0
tons_truck_transport = 0
tons_train_transport = 0
total_tons = 0
for load in range(loads_count):
    tonnage = int(input())
    total_tons += tonnage
    if tonnage < 4:
        tons_bus_transport += tonnage
    elif 3 < tonnage < 12:
        tons_truck_transport += tonnage
    else:
        tons_train_transport += tonnage
bus_cost = bus_price * tons_bus_transport
truck_cost = truck_price * tons_truck_transport
train_cost = train_price * tons_train_transport
total_cost = bus_cost + truck_cost + train_cost
avg_price = total_cost / total_tons
print(f'{avg_price:.2f}')
print(f'{tons_bus_transport / total_tons * 100:.2f}%')
print(f'{tons_truck_transport / total_tons * 100:.2f}%')
print(f'{tons_train_transport / total_tons * 100:.2f}%')