def collect(inv, itm):
    if itm in inv:
        return
    return inv.append(itm)


def drop(inv, itm):
    if itm in inv:
        return inv.remove(itm)
    return


def combine(inv, itm):
    old_itm, new_itm = itm.split(":")
    if old_itm in inv:
        indx = inv.index(old_itm)
        return inv.insert(indx + 1, new_itm)
    return


def renew(inv, itm):
    if itm in inv:
        inv.remove(itm)
        return inv.append(itm)
    return


inventory = input().split(", ")
command = input()
while not command == "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        collect(inventory, item)
    elif action == "Drop":
        drop(inventory, item)
    elif action == "Combine Items":
        combine(inventory, item)
    elif action == "Renew":
        renew(inventory, item)
    command = input()
print(*inventory, sep=", ")
