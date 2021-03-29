soldiers_count = input().split(" ")
steps = int(input())
order_of_killing = []
step = 1
index = 0
while len(soldiers_count):
    if step % steps == 0:
        order_of_killing.append(soldiers_count[index])
        soldiers_count.pop(index)

    else:
        index += 1
    step += 1
    if index >= len(soldiers_count):
        index = 0
print(str(order_of_killing).replace(' ','').replace('\'',''))