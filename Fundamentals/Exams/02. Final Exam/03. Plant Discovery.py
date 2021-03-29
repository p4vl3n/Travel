n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if not plant in plants:
        plants[plant] = {'rarity': 0, 'rating': []}
        plants[plant]['rarity'] = rarity
    else:
        plants[plant]['rarity'] = rarity
command = input()
while not command == "Exhibition":
    action, info = command.split(": ")
    if action == "Rate":
        try:
            flower, rating = info.split(" - ")
            rating = int(rating)
            plants[flower]['rating'].append(rating)
        except:
            print("error")
    elif action == "Update":
        try:
            flower, rarity = info.split(" - ")
            rarity = int(rarity)    
            plants[flower]['rarity'] = rarity
        except:
            print("error")
    elif action == "Reset":
        try:
            flower = info
            plants[flower]['rating'] = []
        except:
            print("error")
    else:
        print("error")
    command = input()
for plant, stats in plants.items():
    if plants[plant]['rating']:
        plants[plant]['av_rating'] = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    else:
        plants[plant]['av_rating'] = 0
sorted_plants = dict(sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['av_rating'])))
print("Plants for the exhibition:")
for plant, stats in sorted_plants.items():
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {plants[plant]['av_rating']:.2f}")
