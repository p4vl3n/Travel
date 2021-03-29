capacity = float(input())
command = str(0)
suitcases = 0
loaded_suitcases = 0
next_suitcase = 0
while command != "End":
    command = input()
    suitcases += 1
    if command == "End":
        print(f'Congratulations! All suitcases are loaded!')
        print(f'Statistic: {loaded_suitcases} suitcases loaded.')
        break
    suitcase_volume = float(command)
    if suitcases % 3 == 0 and suitcases != 0:
        suitcase_volume *= 1.10
    if capacity >= suitcase_volume:
        loaded_suitcases += 1
    else:
        print(f'No more space!')
        print(f'Statistic: {loaded_suitcases} suitcases loaded.')
        break
    capacity -= suitcase_volume
