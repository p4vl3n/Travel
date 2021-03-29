from sys import maxsize
command = input()
min_num = maxsize
while command != "Stop":
    number = int(command)
    if number > min_num:
        min_num = number
    command = input()
print(min_num)