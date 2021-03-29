legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
legendary_components = {'motes': 0, 'shards': 0, 'fragments': 0}
simple_components = {}

found_a_winner = False
winner = ""

while not found_a_winner:
    materials = list(input().split())
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()
        if material in legendary_items:
            legendary_components[material] += quantity
            for component, value in legendary_components.items():
                if value >= 250:
                    legendary_components[component] -= 250
                    winner = legendary_items[component]
                    found_a_winner = True
                    break
        else:
            if material in simple_components:
                simple_components[material] += quantity
            else:
                simple_components[material] = quantity
        if found_a_winner:
            break

sorted_legendary = dict(sorted(legendary_components.items(), key=lambda x: (-x[1], x[0])))
sorted_simple = dict(sorted(simple_components.items(), key=lambda x: x[0]))
print(f"{winner} obtained!")
for x, y in sorted_legendary.items():
    print(f"{x}: {y}")
for x, y in sorted_simple.items():
    print(f"{x}: {y}")