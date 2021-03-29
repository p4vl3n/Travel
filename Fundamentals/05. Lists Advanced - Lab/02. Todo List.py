to_do = []
notes = input()
action_list = []
while not notes == "End":
    action_list = notes.split("-")
    priority = int(action_list[0])
    note = action_list[1]
    to_do.insert(priority, note)
    notes = input()
result = []
for element in to_do:
    if element != 0:
        result.append(element)
print(result)
print(to_do)