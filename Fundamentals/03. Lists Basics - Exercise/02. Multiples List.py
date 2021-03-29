factor = int(input())
count = int(input())
new_list = []
for i in range(factor, factor * count + 1, factor):
    new_list.append(i)
print(new_list)