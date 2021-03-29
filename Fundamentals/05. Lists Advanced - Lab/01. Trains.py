wagons = int(input())
train = []
for wagon in range(wagons):
    train.append(0)

action_list = []
command = input()
while not command == "End":
    action_list = command.split(" ")
    if action_list[0] == "add":
        train[-1] += int(action_list[1])
    elif action_list[0] == "insert":
        train[int(action_list[1])] += int(action_list[2])
    elif action_list[0] == "leave":
        train[int(action_list[1])] -= int(action_list[2])
    command = input()
print(train)