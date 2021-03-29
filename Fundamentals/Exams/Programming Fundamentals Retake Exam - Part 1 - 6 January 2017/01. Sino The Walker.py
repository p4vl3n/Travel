class Watch:
    def __init__(self, hours: int, minutes: int, seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

departure_time = input().split(":")
hour, minute, second = int(departure_time[0]), int(departure_time[1]), int(departure_time[2])
time = Watch(hour, minute, second)
steps = int(input())
second_per_step = int(input())
total_seconds = steps * second_per_step
for second in range(1, total_seconds + 1):
    if time.seconds < 59:
        time.seconds += 1
    elif time.seconds == 59:
        time.seconds = 0
        if time.minutes < 59:
            time.minutes += 1
        elif time.minutes == 59:
            time.minutes = 0
            if time.hours < 23:
                time.hours += 1
            elif time.hours == 23:
                time.hours = 0

print(f"Time of arrival: {time.hours:02d}:{time.minutes:02d}:{time.seconds:02d}")





