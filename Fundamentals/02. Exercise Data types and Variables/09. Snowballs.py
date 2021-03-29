num_of_snowballs = int(input())
best_value = 0
best_snow = 0
best_time = 0
best_quality = 0
for snowball in range(num_of_snowballs):
    snow = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = (snow / time) ** quality
    if snowball_value >= best_value:
        best_value = snowball_value
        best_snow = snow
        best_time = time
        best_quality = quality
print(f"{best_snow} : {best_time} = {int(best_value)} ({best_quality})")
