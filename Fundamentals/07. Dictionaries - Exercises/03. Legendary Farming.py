def reach(legendary_items):
    item = ""
    for key, value in legendary_items.items():
        if value > 250:
            global found_a_winner
            found_a_winner = True
            if key == "shards":
                item = "Shadowmourne"
            elif key == "fragments":
                item = "Valanyr"
            elif key == "motes":
                item = "Dragonwrath"
            legendary_items[key] -= 250
            return item, legendary_items
    return item, legendary_items


def adding_leg_item(mat, quant, itms):
    if mat not in itms:
        itms[mat] = quant
        return
    itms[mat] += quant
    return


legendary_item = ""
simple_components = {}
legendary_components = {}

found_a_winner = False

while not found_a_winner:
    materials = list(input().split())

    for i in range(1, len(materials), 2):
        material = materials[i].lower()
        quantity = int(materials[i - 1])
        if material == "shards" or material == "fragments" or material == "motes" :
            adding_leg_item(material, quantity, legendary_components)
            legendary_item, legendary_components = reach(legendary_components)
            if found_a_winner:
                break
        else:
            adding_leg_item(material, quantity, simple_components)


sorted_legendary = dict(sorted(legendary_components.items(), key=lambda x: (-x[1], x[0])))
sorted_simple = dict(sorted(simple_components.items(), key=lambda x: x[1]))
print(f"{legendary_item} obtained!")
for x, y in sorted_legendary.items():
    print(f"{x}: {y}")
for x, y in sorted_simple.items():
    print(f"{x}: {y}")
