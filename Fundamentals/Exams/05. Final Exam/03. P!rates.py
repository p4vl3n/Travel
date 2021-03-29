class City:
    def __init__(self, city_name, population: int, gold: int):
        self.city_name = city_name
        self.population = int(population)
        self.gold = int(gold)

cities = []
command = input()
while not command == "Sail":
    c_n, ppl, gld = command.split("||") 
    if not [c for c in cities if c.city_name == c_n]:
        city = City(c_n, int(ppl), int(gld))
        cities.append(city)
    else:
        city = [c for c in cities if c.city_name == c_n][0]
        city.gold += int(gld)
        city.population += int(ppl)
    command = input()

command = input()
while not command == "End":
    data = command.split("=>")
    action, town = data[0], data[1]
    city = [c for c in cities if town == c.city_name][0]
    if action == "Plunder":
        people, gold = int(data[2]), int(data[3])
        city.gold -= gold
        city.population -= people
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if city.population < 1 or city.gold < 1:
            cities.remove(city)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        gold = int(data[2])
        if gold >= 0:
            city.gold += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city.gold} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    command = input()

if cities:
    sorted_cities = sorted(cities, key= lambda c: (-c.gold, c.city_name))
    print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")
    for city in sorted_cities:
        print(f"{city.city_name} -> Population: {city.population} citizens, Gold: {city.gold} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

