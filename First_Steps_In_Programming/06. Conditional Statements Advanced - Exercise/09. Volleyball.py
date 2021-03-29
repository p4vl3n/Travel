# ако не пътува и не е на работа - играе в Събота (ден 6ти) + 2/3 от празниците
# пътува N пъти до родния си град
# Когато пътува играе в Неделя
# Влади почива в 3/4 от уикендите
# уикендите = 48
# високосна = 15% повече игра
from math import floor
year = input()
holidays = int(input())
trips = int(input())
weekends = 48
working_weekends = 48 - trips
play_times = (3/4 * working_weekends) + (2/3 * holidays) + trips
if year == "leap":
    play_times *= 1.15
print(floor(play_times))

