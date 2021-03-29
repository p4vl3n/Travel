import math
length = float(input())
width = float(input())
chair_count_lenght = math.floor(length / 1.2)
chair_count_width = math.floor((width - 1) / 0.7)
total_chair_count = chair_count_width * chair_count_lenght - 3
print(total_chair_count)
