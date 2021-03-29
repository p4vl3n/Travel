import re

participants = input().split(", ")
racers_and_scores = {}
for participant in participants:
    racers_and_scores[participant] = 0
name_pattern = r"[a-zA-Z]"
distance_pattern = r"[0-9]"
results = input()
while not results == "end of race":
    possible_participant = re.findall(name_pattern, results)
    participant = "".join(possible_participant)
    if participant in participants:
        score = re.findall(distance_pattern, results)
        for distance in score:
            racers_and_scores[participant] += int(distance)
    results = input()
sorted_racers = dict(sorted(racers_and_scores.items(), key= lambda x: -x[1]))
place = 1
ordered_racers = []
for racer in sorted_racers:
    if place <= 3:
        ordered_racers.append(racer)
        place += 1
print(f"1st place: {ordered_racers[0]}")
print(f"2nd place: {ordered_racers[1]}")
print(f"3rd place: {ordered_racers[2]}")