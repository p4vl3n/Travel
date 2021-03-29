lenght = int(input())
width = int(input())
height = int(input())
displaced_volume_percentage = float(input())
volume = lenght * width * height
total_litres = volume * 0.001
print(total_litres - (total_litres * displaced_volume_percentage/100))